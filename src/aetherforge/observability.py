# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

import json
import time
import logging
import os
from .security_layer import PQCSecurity

class AuditLogger:
    def __init__(self):
        self.log_file = "audit.log"
        self.pqc_security = PQCSecurity()
        logging.basicConfig(level=logging.INFO)
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w') as f:
                f.write("")

    def log_event(self, event_type, details):
        try:
            event = {
                "timestamp": time.time(),
                "type": event_type,
                "who": os.getlogin(),
                "what": details,
                "outcome": "success"
            }
            event_str = json.dumps(event)
            # Sign for immutability
            signature = self.pqc_security.sign_message(event_str.encode(), self._get_secret_key())
            with open(self.log_file, 'a') as f:
                f.write(f"{event_str} | signature: {signature.hex()}\n")
        except Exception as e:
            logging.error(f"Audit logging failed: {str(e)}")
            event["outcome"] = "failure"
            with open(self.log_file, 'a') as f:
                f.write(json.dumps(event) + "\n")  # Fallback unsigned

    def _get_secret_key(self):
        # Simulate vault; in prod, use secure retrieval, no logging
        if os.path.exists("secret_key.bin"):
            with open("secret_key.bin", 'rb') as f:
                return f.read()
        raise FileNotFoundError("Secret key missing")

    def export_audit(self, filters=None):
        try:
            with open(self.log_file, 'r') as f:
                logs = f.readlines()
            if filters:
                logs = [log for log in logs if all(k in log for k in filters)]
            return logs
        except Exception as e:
            logging.error(f"Audit export failed: {str(e)}")
            return []

# SLOs: Latency < 100ms, success > 99%, error budget 1% monthly

# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.