# Workflow: Write a professional & friendly email

## Objective
Draft an email that sounds professional yet warm and friendly, then save it to
`.tmp/` for review. The agent writes the content; `tools/save_email.py` persists
it deterministically.

## Inputs
- `recipient` (**required**) — the recipient's email address.
  **If not provided, ASK the user for it before doing anything else.**
- `purpose` — what the email is about / key points to convey. If unclear, ask.
- `subject` — optional; draft one from the purpose if not given.
- `cc`, `sender` — optional.

## Tone guidelines
- Professional but warm — never stiff or robotic, never overly casual.
- Open with a friendly, personable greeting; close politely (e.g. "Best,").
- Be clear and concise; lead with the main point, keep paragraphs short.
- Courteous and positive; use the recipient's name when known.
- Plain, natural language. No jargon, no filler, no exclamation overload.

## Steps
1. Confirm the **recipient email address**. If missing → ask the user.
2. Confirm the **purpose / key points**. If unclear → ask.
3. Draft the subject and body following the tone guidelines above.
4. Run the tool to save the draft:
   ```bash
   python3 tools/save_email.py \
       --to "<recipient>" \
       --subject "<subject>" \
       --body-file <path-in-scratchpad-or-.tmp> \
       [--cc "a@x.com,b@y.com"] [--from "<sender>"]
   ```
   (Use `--body "..."` for short inline bodies.)
5. Show the user the saved file path and the drafted email; offer to revise.

## Outputs
- `.tmp/email_<timestamp>_<subject-slug>.txt` — readable draft with headers.
- `.tmp/email_<timestamp>_<subject-slug>.json` — structured metadata.

## Edge cases & notes
- The tool validates `--to` and `--cc`; an invalid address exits non-zero with a
  JSON error on stderr. Fix the address and rerun.
- Body via `--body` (inline) or `--body-file` (path) — they're mutually exclusive.
- No API keys / external calls — pure stdlib, safe to run freely.
