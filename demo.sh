#!/bin/bash
# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

set -euo pipefail
trap 'echo "Self-healing: Error at line $LINENO — retrying..."; sleep 2; exec "$0" "$@"' ERR

echo "AetherForge EULA: By running this, you accept terms."
read -p "Accept? (y/n): " accept
[[ "$accept" == "y" ]] || exit 0

echo "License valid (Free tier active)"
python3 - <<'PY'
from datetime import datetime; print("Monetization event:", {"receipt": "local-demo-123", "tier": "Free"})
print("Agents running:", [x*x for x in range(4)])
print("Build & deploy simulation: success")
PY

echo "Demo complete — no GitHub required"
