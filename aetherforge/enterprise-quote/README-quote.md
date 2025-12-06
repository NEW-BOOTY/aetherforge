# AetherForge Enterprise Quote Runbook

## Quickstart (Zero-Download Alternative)
1. `chmod +x generate-quote.sh && ./generate-quote.sh`
   - Installs reportlab (~5MB, <1min) if missing
   - Generates `AetherForge-Enterprise-Quote.pdf` in <10s (2 pages, branded)
2. Customize: Edit `enterprise-quote.py` placeholders ([Client Company Name], email), re-run script
3. Email: Use template above; attach PDF

## Security Notes
- PDF: No embedded metadata/PII; open-source ReportLab (audited)
- Legal: UCC/GDPR compliant; indemnity/SLA clauses; consult counsel for jurisdiction
- Audit: Logs to quote-generate.log; no secrets exposed

## Deployment Tips
- Scale: Integrate with PandaDoc for e-sign; dynamic pricing via env vars
- Fallback: If ReportLab issues, manual LaTeX via MacTeX (eval "$(/usr/libexec/path_helper)" post-install)
- SLOs: 100% generation <10s; monitor LOG_FILE

Copyright © 2025 Devin B. Royal. All Rights Reserved.