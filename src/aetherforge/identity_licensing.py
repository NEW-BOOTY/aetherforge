# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

import json
import os
from datetime import datetime, timedelta
from .security_layer import PQCSecurity
import logging

class LicenseValidator:
    def __init__(self):
        self.pqc_security = PQCSecurity()
        self.license_file = "license.json"
        self.grace_period = timedelta(days=7)
        logging.basicConfig(level=logging.INFO)

    def is_valid(self, required_tier):
        try:
            if not os.path.exists(self.license_file):
                raise FileNotFoundError("License file missing")
            with open(self.license_file, 'r') as f:
                license_data = json.load(f)
            # Validate signature using PQC
            signature = license_data.pop('signature')
            data_bytes = json.dumps(license_data).encode()
            if not self.pqc_security.verify_signature(data_bytes, signature):
                raise ValueError("Invalid license signature")
            expiry = datetime.fromisoformat(license_data['expiry'])
            if datetime.now() > expiry + self.grace_period:
                raise ValueError("License expired")
            tier = license_data['tier']
            tiers = {'Free': 1, 'Pro': 2, 'Enterprise': 3}
            if tiers.get(tier, 0) < tiers.get(required_tier, 0):
                raise ValueError("Insufficient license tier")
            return True
        except Exception as e:
            logging.error(f"License validation failed: {str(e)}")
            return False

# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.