---
name: ats-sender-patterns
description: Reliable ATS domains and company recruiting addresses for automated job-application reply detection
metadata:
  type: reference
---

## ATS Platform Domains (high-confidence — every message from these is a job-application reply)
- `greenhouse-mail.io` (Greenhouse ATS)
- `hire.lever.co`, `lever.co` (Lever ATS)
- `ashbyhq.com` (Ashby ATS) — but watch for real-person emails from named employees at ashbyhq.com
- `myworkday.com` (Workday ATS — covers many companies: Manulife, Clio, RBC, Autodesk, Thomson Reuters, Equifax, Workday itself, State Street, AstraZeneca, Interac, etc.)
- `successfactors.com` (SAP SuccessFactors — McCain Foods, McCormick, Ontario Power Generation)
- `gem.com`, `appreview.gem.com` (Gem CRM/ATS — Apartment List, Dropbox)
- `oraclerecruitingcloud@ritchiebros.com` (Oracle Recruiting Cloud via RB Global)
- `applytojob.com` (ApplyToJob ATS — WELL Health)
- `amazon.jobs`, `mail.amazon.jobs` (Amazon ATS)
- `jobvite.com`, `notification@jobvite.com`, `no-reply@jobvite.com` (Jobvite ATS — Confluent, CARFAX, Splunk)

## Company-Specific Recruiting Addresses (high-confidence)
- `me@scotiabank.com` (Scotiabank Recruitment)
- `EAcareers@ea.com` (Electronic Arts)
- `no-reply-recruiting@robinhood.com` (Robinhood)
- `no-reply@okta.com` (Okta)
- `no-reply@architech.ca` (Architech)
- `careers@gusto.com` (Gusto)
- `careers@pathcore.freshteam.com` (Pathcore — Freshteam ATS)
- `noreply@mail.amazon.jobs` (Amazon automated notifications)

## Confirmed False Positives (do NOT label)
- `noreply@github.com` — GitHub OAuth "application" authorization alerts (not job applications)
- `noreply@epan.proteantech.in` — PAN card government application
- `noreply@medium.com` — newsletter articles mentioning "application"
- Real human recruiter emails even if from ATS domains (e.g., `chotakk@amazon.jobs`, `josh.bourke@ashbyhq.com`, `nicomagana@lyft.com`, `andrewpickup@google.com`)
- Interview scheduling / NDA signing messages from real recruiters via ATS relay (e.g., Jada Grier at Confluent via jobvite)
- Lever calendar-invite style confirmations ("Your Interview Scheduled for...")
