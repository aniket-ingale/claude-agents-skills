#!/usr/bin/env python3
"""Save a composed email draft to the .tmp/ folder.

The agent writes the professional + friendly email content; this tool handles
the deterministic part: validating the recipient address and persisting the
draft as both a human-readable .txt and a .json metadata file.

Usage:
    python3 tools/save_email.py \
        --to "jane@example.com" \
        --subject "Quick follow-up on our chat" \
        --body-file /path/to/body.txt \
        [--cc "a@x.com,b@y.com"] [--from "me@example.com"]

Body can be passed via --body (inline) or --body-file (path). Prints a JSON
object with the saved file paths to stdout. Exits non-zero on error.
"""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

# Repo root is the parent of tools/, so .tmp/ is a sibling of this script's dir.
TMP_DIR = Path(__file__).resolve().parent.parent / ".tmp"

EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def valid_email(addr: str) -> bool:
    return bool(EMAIL_RE.match(addr.strip()))


def parse_addr_list(raw: str):
    return [a.strip() for a in raw.split(",") if a.strip()]


def slugify(text: str, max_len: int = 40) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len] or "email"


def fail(msg: str):
    print(json.dumps({"ok": False, "error": msg}), file=sys.stderr)
    sys.exit(1)


def main():
    p = argparse.ArgumentParser(description="Save an email draft to .tmp/")
    p.add_argument("--to", required=True, help="Recipient email address")
    p.add_argument("--subject", required=True, help="Email subject line")
    g = p.add_mutually_exclusive_group(required=True)
    g.add_argument("--body", help="Email body as an inline string")
    g.add_argument("--body-file", help="Path to a file containing the body")
    p.add_argument("--cc", help="Comma-separated CC addresses", default="")
    p.add_argument("--from", dest="sender", help="Sender address", default="")
    args = p.parse_args()

    if not valid_email(args.to):
        fail(f"Invalid recipient email address: {args.to!r}")

    cc = parse_addr_list(args.cc)
    bad_cc = [a for a in cc if not valid_email(a)]
    if bad_cc:
        fail(f"Invalid CC address(es): {bad_cc}")

    if args.body_file:
        body_path = Path(args.body_file)
        if not body_path.is_file():
            fail(f"Body file not found: {args.body_file}")
        body = body_path.read_text(encoding="utf-8")
    else:
        body = args.body

    TMP_DIR.mkdir(parents=True, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    stem = f"email_{ts}_{slugify(args.subject)}"
    txt_path = TMP_DIR / f"{stem}.txt"
    json_path = TMP_DIR / f"{stem}.json"

    header_lines = [f"To: {args.to}"]
    if cc:
        header_lines.append(f"Cc: {', '.join(cc)}")
    if args.sender:
        header_lines.append(f"From: {args.sender}")
    header_lines.append(f"Subject: {args.subject}")
    readable = "\n".join(header_lines) + "\n\n" + body.rstrip() + "\n"
    txt_path.write_text(readable, encoding="utf-8")

    meta = {
        "to": args.to.strip(),
        "cc": cc,
        "from": args.sender.strip(),
        "subject": args.subject,
        "body": body,
        "created_at": datetime.now().isoformat(timespec="seconds"),
    }
    json_path.write_text(json.dumps(meta, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps({
        "ok": True,
        "txt_path": str(txt_path),
        "json_path": str(json_path),
    }, indent=2))


if __name__ == "__main__":
    main()
