---
name: search-strategy
description: Gmail search strategy, API behavior, and pagination approach for job-application triage
metadata:
  type: reference
---

## Search Tool Behavior
- `searchGmail` hard-caps results at 20 per query regardless of `maxResults` parameter
- Total estimates shown ("Total estimate: N messages") are approximate and often inaccurate
- For months with >20 matching messages, use monthly sub-buckets; for >20 in a month, use bi-weekly buckets

## Efficient Query Pattern
Primary ATS domain query (combine in one OR clause):
```
(from:greenhouse-mail.io OR from:lever.co OR from:ashbyhq.com OR from:myworkday.com OR from:successfactors.com OR from:gem.com OR from:oraclerecruitingcloud OR from:applytojob.com OR from:amazon.jobs OR from:jobvite.com) after:YYYY/M/D before:YYYY/M/D
```
Supplement with company-specific addresses not covered by ATS domains (Scotiabank, EA, Robinhood, Okta, Architech, Gusto, Pathcore).

## Date Window
- "Older than 6 months" = received before 2025-12-27 (from 2026-06-27 session date)
- Use explicit `after:` / `before:` date ranges rather than `older_than:Nm` for precise pagination
- Batch by month; sub-batch if month has >20 messages (busy months: Jul-Oct 2024, Jan-Feb 2025)

## Labeling
- Use `batchAddGmailLabels` (max 1000 IDs per call) — much more efficient than one-by-one
- Operation is idempotent: re-applying an existing label is a no-op, safe to include already-labeled messages
- Three batches of ~90 each worked cleanly in this session (277 total)

## Typical Volume (Aniket's inbox, Jul 2024 – Dec 2025)
- ~277 qualifying messages across 18 months
- Busiest months: July 2024 (~30), August 2024 (~30), September 2024 (~28), January 2025 (~40+), February 2025 (~50+)
- Sparse after June 2025 (job search winding down or paused)
