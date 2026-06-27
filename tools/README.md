# Tools — Layer 3 (Execution)

Deterministic Python scripts that do the actual work: API calls, data
transformations, file operations, database queries.

## Conventions

- One script per discrete task. Keep them small, testable, and fast.
- Load credentials from `.env` (via `python-dotenv`) — never hardcode secrets.
- Accept inputs as CLI args (`argparse`); print machine-readable output
  (JSON to stdout) so the agent can parse results.
- Write intermediate artifacts to `.tmp/`, not the repo root.
- Exit non-zero with a clear message on failure so the agent can recover.

## Adding a tool

1. Check whether an existing tool already covers the task.
2. Write the script here.
3. Reference it from the relevant workflow in `workflows/`.
