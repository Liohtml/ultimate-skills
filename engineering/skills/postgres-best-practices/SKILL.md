---
name: postgres-best-practices
description: Postgres rules with incorrect-vs-correct SQL for schema design, indexes, queries, connection pooling, Row-Level Security, locking, and safe migrations; loads only the rule files a task needs. Use before writing or changing anything that lives in a Postgres database (tables, column types, constraints, indexes, RLS policies, migrations, bulk loads, queue tables), and when diagnosing slow queries, EXPLAIN plans, connection exhaustion, lock contention, deadlocks, bloat, or rows visible to the wrong tenant. Also covers zero-downtime migrations (lock_timeout, CREATE INDEX CONCURRENTLY, expand/contract), backup/restore and major-version upgrades. For app-level profiling and Core Web Vitals use performance-optimization; for API shape use api-and-interface-design; for broader application security use security-and-hardening.
license: MIT (rule files from supabase/agent-skills); references/ops-backup-restore.md, ops-major-version-upgrades.md and the adapted table in ops-migration-safety.md are Apache-2.0 (see LICENSE-neon-apache-2.0.txt)
---

# Postgres Best Practices

> Rule files adapted from [supabase/agent-skills `supabase-postgres-best-practices`](https://github.com/supabase/agent-skills/tree/8331f910845103c08d51f6ca1d86ebb7d1f745e3/skills/supabase-postgres-best-practices) (MIT, Copyright (c) 2026 Supabase; renamed to a vendor-neutral skill, router rewritten). Operations references adapted from [neondatabase/postgres-skills](https://github.com/neondatabase/postgres-skills/tree/27fe45e0f71ea89a6eaf9ea4d2e4068957c81c26/skills/postgres-best-practices) (Apache-2.0, modified). `ops-migration-safety.md` written for this marketplace.

Rules for Postgres running anywhere (self-hosted, RDS, Cloud SQL, Neon, Supabase, …), prioritized by impact. Some rule files carry "Supabase-specific notes"; apply them only on Supabase.

## How to Use

1. **Do not read every file.** Pick the category from the task, then open only the 1-3 rule files that match.
2. Each rule file has: why it matters, an **incorrect** SQL example, a **correct** SQL example, and often the EXPLAIN output or metric that proves the difference.
3. When you change a query or index, prove the effect: run `EXPLAIN (ANALYZE, BUFFERS)` before and after ([monitor-explain-analyze.md](references/monitor-explain-analyze.md)) on realistic data volumes, and report both plans.
4. Any DDL against a table with production traffic: read [ops-migration-safety.md](references/ops-migration-safety.md) first.

| If the task is… | Start with |
|---|---|
| New table / column types / keys | `schema-data-types`, `schema-primary-keys`, `schema-foreign-key-indexes`, `schema-constraints` |
| A migration on a live table | `ops-migration-safety`, `schema-constraints` |
| A slow query | `monitor-explain-analyze`, `query-missing-indexes`, `query-composite-indexes`, `data-n-plus-one` |
| Multi-tenant data / "user sees other user's rows" | `security-rls-basics`, `security-rls-performance`, `security-privileges` |
| "Too many connections" / timeouts under load | `conn-pooling`, `conn-limits`, `conn-idle-timeout`, `conn-prepared-statements` |
| Job queue / worker table | `lock-skip-locked`, `lock-short-transactions`, `lock-advisory` |
| Deadlocks or lock waits | `lock-deadlock-prevention`, `lock-short-transactions` |
| Bulk import / pagination / upserts | `data-batch-inserts`, `data-pagination`, `data-upsert` |
| Backups, restores, PITR, `pg_dump`/`pg_restore` | `ops-backup-restore` |
| Upgrading Postgres major version | `ops-major-version-upgrades` |

## Rule Index

### Query Performance (`query-`, CRITICAL)

| Rule file | Rule | Impact |
|---|---|---|
| [query-composite-indexes.md](references/query-composite-indexes.md) | Create Composite Indexes for Multi-Column Queries | HIGH |
| [query-covering-indexes.md](references/query-covering-indexes.md) | Use Covering Indexes to Avoid Table Lookups | MEDIUM-HIGH |
| [query-index-types.md](references/query-index-types.md) | Choose the Right Index Type for Your Data | HIGH |
| [query-missing-indexes.md](references/query-missing-indexes.md) | Add Indexes on WHERE and JOIN Columns | CRITICAL |
| [query-partial-indexes.md](references/query-partial-indexes.md) | Use Partial Indexes for Filtered Queries | HIGH |

### Connection Management (`conn-`, CRITICAL)

| Rule file | Rule | Impact |
|---|---|---|
| [conn-idle-timeout.md](references/conn-idle-timeout.md) | Configure Idle Connection Timeouts | HIGH |
| [conn-limits.md](references/conn-limits.md) | Set Appropriate Connection Limits | CRITICAL |
| [conn-pooling.md](references/conn-pooling.md) | Use Connection Pooling for All Applications | CRITICAL |
| [conn-prepared-statements.md](references/conn-prepared-statements.md) | Use Prepared Statements Correctly with Pooling | HIGH |

### Security & RLS (`security-`, CRITICAL)

| Rule file | Rule | Impact |
|---|---|---|
| [security-privileges.md](references/security-privileges.md) | Apply Principle of Least Privilege | MEDIUM |
| [security-rls-basics.md](references/security-rls-basics.md) | Enable Row Level Security for Multi-Tenant Data | CRITICAL |
| [security-rls-performance.md](references/security-rls-performance.md) | Optimize RLS Policies for Performance | HIGH |

### Schema Design (`schema-`, HIGH)

| Rule file | Rule | Impact |
|---|---|---|
| [schema-constraints.md](references/schema-constraints.md) | Add Constraints Safely in Migrations | HIGH |
| [schema-data-types.md](references/schema-data-types.md) | Choose Appropriate Data Types | HIGH |
| [schema-foreign-key-indexes.md](references/schema-foreign-key-indexes.md) | Index Foreign Key Columns | HIGH |
| [schema-lowercase-identifiers.md](references/schema-lowercase-identifiers.md) | Use Lowercase Identifiers for Compatibility | MEDIUM |
| [schema-partitioning.md](references/schema-partitioning.md) | Partition Large Tables for Better Performance | MEDIUM-HIGH |
| [schema-primary-keys.md](references/schema-primary-keys.md) | Select Optimal Primary Key Strategy | HIGH |

### Concurrency & Locking (`lock-`, MEDIUM-HIGH)

| Rule file | Rule | Impact |
|---|---|---|
| [lock-advisory.md](references/lock-advisory.md) | Use Advisory Locks for Application-Level Locking | MEDIUM |
| [lock-deadlock-prevention.md](references/lock-deadlock-prevention.md) | Prevent Deadlocks with Consistent Lock Ordering | MEDIUM-HIGH |
| [lock-short-transactions.md](references/lock-short-transactions.md) | Keep Transactions Short to Reduce Lock Contention | MEDIUM-HIGH |
| [lock-skip-locked.md](references/lock-skip-locked.md) | Use SKIP LOCKED for Non-Blocking Queue Processing | MEDIUM-HIGH |

### Data Access Patterns (`data-`, MEDIUM)

| Rule file | Rule | Impact |
|---|---|---|
| [data-batch-inserts.md](references/data-batch-inserts.md) | Batch INSERT Statements for Bulk Data | MEDIUM |
| [data-n-plus-one.md](references/data-n-plus-one.md) | Eliminate N+1 Queries with Batch Loading | MEDIUM-HIGH |
| [data-pagination.md](references/data-pagination.md) | Use Cursor-Based Pagination Instead of OFFSET | MEDIUM-HIGH |
| [data-upsert.md](references/data-upsert.md) | Use UPSERT for Insert-or-Update Operations | MEDIUM |

### Monitoring & Diagnostics (`monitor-`, LOW-MEDIUM)

| Rule file | Rule | Impact |
|---|---|---|
| [monitor-explain-analyze.md](references/monitor-explain-analyze.md) | Use EXPLAIN ANALYZE to Diagnose Slow Queries | LOW-MEDIUM |
| [monitor-pg-stat-statements.md](references/monitor-pg-stat-statements.md) | Enable pg_stat_statements for Query Analysis | LOW-MEDIUM |
| [monitor-vacuum-analyze.md](references/monitor-vacuum-analyze.md) | Maintain Table Statistics with VACUUM and ANALYZE | MEDIUM |

### Advanced Features (`advanced-`, LOW)

| Rule file | Rule | Impact |
|---|---|---|
| [advanced-full-text-search.md](references/advanced-full-text-search.md) | Use tsvector for Full-Text Search | MEDIUM |
| [advanced-jsonb-indexing.md](references/advanced-jsonb-indexing.md) | Index JSONB Columns for Efficient Querying | MEDIUM |

### Operations: Migrations, Backup, Upgrades (`ops-`, CRITICAL)

| Rule file | Rule | Impact |
|---|---|---|
| [ops-backup-restore.md](references/ops-backup-restore.md) | Backup & Restore Reference | - |
| [ops-major-version-upgrades.md](references/ops-major-version-upgrades.md) | Major Version Upgrades Reference | - |
| [ops-migration-safety.md](references/ops-migration-safety.md) | Ship Schema Migrations Without Locking Production | CRITICAL |

## References

- https://www.postgresql.org/docs/current/
- https://wiki.postgresql.org/wiki/Performance_Optimization
- https://supabase.com/docs/guides/database/overview
