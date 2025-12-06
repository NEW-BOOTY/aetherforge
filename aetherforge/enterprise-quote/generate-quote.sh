#!/bin/bash
# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

set -euo pipefail
LOG_FILE="quote-generate.log"
exec > >(tee -a "$LOG_FILE") 2>&1

# Self-healing: Install reportlab if missing, retry compilation
retry() { local n=3; until "$@"; do ((n--)) || return 1; sleep $((2** (3-n))); done; }

timestamp() { echo "[$(date -u +'%Y-%m-%dT%H:%M:%SZ')] $1"; }

timestamp "Starting AetherForge Enterprise Quote PDF generation (ReportLab alternative)"

# Defensive: Install reportlab if missing (lightweight, <1min)
if ! python3 -c "import reportlab" 2>/dev/null; then
  timestamp "reportlab missing — installing via pip"
  retry python3 -m pip install reportlab || {
    timestamp "pip install failed — using user mode"
    retry python3 -m pip install --user reportlab
  }
fi

# Run Python generator (deterministic, <10s)
retry python3 enterprise-quote.py || {
  timestamp "Generation failed — cleaning and retry"
  rm -f AetherForge-Enterprise-Quote.pdf
  retry python3 enterprise-quote.py
}

# Validation: Check PDF exists and size >20KB (non-empty)
if [[ -f "AetherForge-Enterprise-Quote.pdf" && $(stat -f%z AetherForge-Enterprise-Quote.pdf 2>/dev/null || stat -c%s AetherForge-Enterprise-Quote.pdf) -gt 20000 ]]; then
  timestamp "✓ PDF generated successfully: AetherForge-Enterprise-Quote.pdf (2 pages)"
  open AetherForge-Enterprise-Quote.pdf  # macOS preview
else
  timestamp "✗ PDF generation failed — check $LOG_FILE"
  exit 1
fi

timestamp "Quote ready. Customize placeholders in enterprise-quote.py and re-run. Email template below."
cat << 'EOF'

## Email Template (Copy-Paste)
Subject: AetherForge Enterprise Quote — $25k Starter / $99k Unlimited

Hi [Name],

Attached is your customized enterprise quote for AetherForge: the governed, PQC-secure agent platform with runtime licensing and monetization.

- Starter: $25k/year (unlimited agents, on-prem)
- Unlimited: $99k/year (multi-tenant, SLA)

30-min demo? Reply or book: [your-calendly-link]

Devin Benard Royal, CTO
github.com/new-booty/aetherforge
Attachment: AetherForge-Enterprise-Quote.pdf

EOF

# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.