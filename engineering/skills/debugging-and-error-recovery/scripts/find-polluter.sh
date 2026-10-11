#!/usr/bin/env bash
# Find which test file creates unwanted files/state by running test files one
# at a time until the artifact appears.
# Adapted from obra/superpowers (MIT, Copyright (c) 2025 Jesse Vincent),
# skills/systematic-debugging/find-polluter.sh @ 5bf4e78. Changes: the test
# runner is configurable via TEST_CMD (default: "npm test"); test paths
# containing spaces are kept intact; the script aborts (exit 2) instead of
# reporting "all tests clean" when the artifact already exists before the
# first test or when no test file matches the pattern.
#
# Usage: TEST_CMD="npx vitest run" ./find-polluter.sh <file_or_dir_to_check> <test_pattern>
# Example: ./find-polluter.sh '.git' 'src/**/*.test.ts'
# Exit: 0 no polluter found, 1 polluter found (or usage error), 2 cannot search

set -e

TEST_CMD="${TEST_CMD:-npm test}"

if [ $# -ne 2 ]; then
  echo "Usage: $0 <file_to_check> <test_pattern>"
  echo "Example: $0 '.git' 'src/**/*.test.ts'"
  exit 1
fi

POLLUTION_CHECK="$1"
TEST_PATTERN="$2"

echo "🔍 Searching for test that creates: $POLLUTION_CHECK"
echo "Test pattern: $TEST_PATTERN"
echo ""

# Get list of test files (find . emits ./-prefixed paths, so accept the
# pattern written with or without a leading ./)
TEST_PATTERN="${TEST_PATTERN#./}"
# find -path can't match '**/' against zero directory levels, so a pattern
# like src/**/*.test.ts would skip src/top.test.ts; also try the pattern
# with '**/' collapsed to cover files directly under the base directory.
# Read into an array (bash 3.2 compatible) so paths with spaces stay intact.
TEST_FILES=()
while IFS= read -r f; do
  TEST_FILES+=("$f")
done < <(find . \( -path "./$TEST_PATTERN" -o -path "./${TEST_PATTERN//\*\*\//}" \) | sort -u)
TOTAL=${#TEST_FILES[@]}

echo "Found $TOTAL test files"
echo ""

if [ "$TOTAL" -eq 0 ]; then
  echo "❌ No test files match '$TEST_PATTERN' (relative to $(pwd)); nothing to search." >&2
  exit 2
fi

if [ -e "$POLLUTION_CHECK" ]; then
  echo "❌ $POLLUTION_CHECK already exists before any test ran; remove it and re-run." >&2
  exit 2
fi

COUNT=0
for TEST_FILE in "${TEST_FILES[@]}"; do
  COUNT=$((COUNT + 1))

  # Skip if pollution already exists
  if [ -e "$POLLUTION_CHECK" ]; then
    echo "⚠️  Pollution already exists before test $COUNT/$TOTAL"
    echo "   Skipping: $TEST_FILE"
    continue
  fi

  echo "[$COUNT/$TOTAL] Testing: $TEST_FILE"

  # Run the test
  $TEST_CMD "$TEST_FILE" > /dev/null 2>&1 || true

  # Check if pollution appeared
  if [ -e "$POLLUTION_CHECK" ]; then
    echo ""
    echo "🎯 FOUND POLLUTER!"
    echo "   Test: $TEST_FILE"
    echo "   Created: $POLLUTION_CHECK"
    echo ""
    echo "Pollution details:"
    ls -la "$POLLUTION_CHECK"
    echo ""
    echo "To investigate:"
    echo "  $TEST_CMD \"$TEST_FILE\"    # Run just this test"
    echo "  cat \"$TEST_FILE\"         # Review test code"
    exit 1
  fi
done

echo ""
echo "✅ No polluter found - all tests clean!"
exit 0
