# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

import unittest
from src.aetherforge.identity_licensing import LicenseValidator
from src.aetherforge.agent_layer import AgentFederation, sample_task
from src.aetherforge.security_layer import PQCSecurity

class TestAetherForge(unittest.TestCase):
    def test_license_valid(self):
        validator = LicenseValidator()
        # Assume test license; in prod, mock file
        self.assertFalse(validator.is_valid('Enterprise'))  # Expected false without file

    def test_agent_exec(self):
        agents = AgentFederation(1)
        result = agents.execute_task(sample_task, (2,))
        self.assertEqual(result, 4)

    def test_pqc_sign_verify(self):
        sec = PQCSecurity()
        pub, sec_key = sec.generate_keypair()
        msg = b"test"
        sig = sec.sign_message(msg, sec_key)
        self.assertTrue(sec.verify_signature(msg, sig, pub))

if __name__ == '__main__':
    unittest.main()

# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.