---
name: label-conventions
description: Gmail label IDs and naming conventions for job-application triage
metadata:
  type: reference
---

- `Jobs` label ID: `Label_3204663346090208429`
- `Jobs/Old Replies` label ID: `Label_28` (sub-label under Jobs, already exists)
- `Jobs/Old Replies` is the canonical archive label for automated job-application replies older than 6 months
- Do NOT create a new label if it already exists — Gmail returns 409; fetch label list first to get ID

**Why:** User already had a `Jobs` label; sub-label keeps archive separate from active tracking.
