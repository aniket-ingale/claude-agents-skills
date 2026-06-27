# Workflows — Layer 1 (Instructions)

Markdown SOPs that brief the agent on how to accomplish a task. Plain language,
the way you'd brief a teammate.

## Each workflow should define

- **Objective** — what success looks like.
- **Inputs** — what's required before starting (params, files, credentials).
- **Tools** — which scripts in `tools/` to run, and in what order.
- **Outputs** — where the deliverable goes (usually a cloud service).
- **Edge cases** — known failure modes, rate limits, timing quirks.

## Keeping workflows current

Workflows evolve as we learn. When you discover a better method or a recurring
issue, update the relevant workflow. Do not create or overwrite workflows
without asking first.

See [_TEMPLATE.md](_TEMPLATE.md) for the starting structure.
