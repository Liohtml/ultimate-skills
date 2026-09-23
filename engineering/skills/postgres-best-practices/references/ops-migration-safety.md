---
title: Ship Schema Migrations Without Locking Production
impact: CRITICAL
impactDescription: Prevents outages from lock queues and table rewrites during deploys
tags: migrations, ddl, locks, lock_timeout, concurrently, expand-contract, zero-downtime
---

## Ship Schema Migrations Without Locking Production

> Written for ultimate-skills. The "Safe column operations" table and the safe `NOT NULL` pattern are adapted from [neondatabase/postgres-skills `schema-design.md` § Migration Safety](https://github.com/neondatabase/postgres-skills/blob/27fe45e0f71ea89a6eaf9ea4d2e4068957c81c26/skills/postgres-best-practices/references/schema-design.md) (Apache-2.0, see `../LICENSE-neon-apache-2.0.txt`; modified: merged with additional guidance). For idempotent `ADD CONSTRAINT` in migration files see [schema-constraints.md](schema-constraints.md).

Most DDL takes an `ACCESS EXCLUSIVE` lock. The danger is rarely the DDL itself; it is the **lock queue**: an `ALTER TABLE` waiting behind one long-running query blocks every later read and write on that table until it gets its lock. An "instant" migration can take the site down this way.

### 1. Always bound lock waits

**Incorrect (waits indefinitely, queueing all traffic behind it):**

```sql
alter table orders add column note text;
```

**Correct (fail fast, retry later):**

```sql
set lock_timeout = '3s';        -- give up if the lock is not granted quickly
set statement_timeout = '15min'; -- upper bound for the whole statement
alter table orders add column note text;
```

Run migrations with a retry loop around `lock_timeout` failures rather than raising the timeout. Check for long-running transactions (`pg_stat_activity` where `xact_start < now() - interval '5 minutes'`) before deploying.

### 2. Build and drop indexes concurrently

```sql
-- Does not block writes; cannot run inside a transaction block
create index concurrently if not exists orders_customer_id_idx on orders (customer_id);
drop index concurrently if exists orders_old_idx;
```

A failed `CREATE INDEX CONCURRENTLY` leaves an `INVALID` index behind: drop it and retry. Many migration tools wrap each file in a transaction; put concurrent index builds in their own non-transactional migration. On partitioned tables, build per partition and attach (see [query-index-types.md](query-index-types.md) and the PostgreSQL docs on `CREATE INDEX ... ON ONLY`).

### 3. Safe column operations

| Operation | Safe online? | Notes |
|-----------|-------------|-------|
| `ADD COLUMN` (nullable, no default) | Yes | Instant metadata change |
| `ADD COLUMN ... DEFAULT x` (constant) | Yes (PG11+) | Default stored in catalog, no table rewrite; volatile defaults such as `random()` still rewrite |
| `DROP COLUMN` | Yes | Marks column as dropped, no rewrite; deploy code that stops reading it first |
| `ALTER COLUMN SET NOT NULL` | Caution | Full table scan under exclusive lock unless a validated `CHECK` exists (pattern below) |
| `ALTER COLUMN TYPE` | No | Usually a full table rewrite plus exclusive lock; use expand/contract |
| `ADD CONSTRAINT ... NOT VALID` | Yes | Does not scan existing rows |
| `VALIDATE CONSTRAINT` | Yes | `SHARE UPDATE EXCLUSIVE` lock: reads and writes continue |
| `ADD FOREIGN KEY` | Caution | Add `NOT VALID`, then `VALIDATE` separately |
| `RENAME COLUMN` / `RENAME TABLE` | Breaking | Fast, but breaks running code; use expand/contract |

### 4. Safe NOT NULL pattern

```sql
-- Step 1: add CHECK without validating existing rows (brief lock)
alter table orders add constraint orders_status_nn
    check (status is not null) not valid;

-- Step 2: validate without blocking reads/writes
alter table orders validate constraint orders_status_nn;

-- Step 3: SET NOT NULL skips the table scan when a valid CHECK proves it (PG12+)
alter table orders alter column status set not null;

-- Step 4: drop the now-redundant CHECK
alter table orders drop constraint orders_status_nn;
```

### 5. Expand / contract for breaking changes

Never rename or retype a column in one deploy. Split it so every step is backward compatible with the code currently running:

1. **Expand**: add the new column / table (nullable, no rewrite).
2. **Dual-write**: deploy code that writes both old and new.
3. **Backfill** in small batches (e.g. 1-10k rows per transaction, keyed by primary key, with a pause between batches) so no long transaction holds locks or bloats WAL.
4. **Switch reads** to the new column; verify.
5. **Contract**: stop writing the old column, then drop it in a later deploy.

### 6. Checklist before running a migration

- [ ] `lock_timeout` set; retry on failure instead of waiting
- [ ] No `ALTER COLUMN TYPE`, rename, or unvalidated `NOT NULL` / FK on a large, hot table
- [ ] Indexes built `CONCURRENTLY`, outside a transaction
- [ ] Backfills batched, not one `UPDATE` over the whole table
- [ ] Rollback path known (and a recent backup / restore point, see [ops-backup-restore.md](ops-backup-restore.md))
- [ ] Tried against a production-sized copy when the table is large

Reference: [ALTER TABLE](https://www.postgresql.org/docs/current/sql-altertable.html), [Explicit Locking](https://www.postgresql.org/docs/current/explicit-locking.html), [CREATE INDEX CONCURRENTLY](https://www.postgresql.org/docs/current/sql-createindex.html#SQL-CREATEINDEX-CONCURRENTLY)
