# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

try:
    from oqs import KeyEncapsulation, Signature
except ImportError:
    raise ImportError("liboqs-python required for PQC; install via pip")

import logging
import os

class PQCSecurity:
    def __init__(self):
        self.kem_algo = "Kyber512"  # PQC key exchange: Kyber for resistance to quantum attacks
        self.sig_algo = "Dilithium2"  # PQC signing: Dilithium for secure signatures
        logging.basicConfig(level=logging.INFO)
        # Rationale: Kyber/Dilithium selected as NIST-standardized, balanced security/performance; mitigates Shor's algorithm threats.

    def generate_keypair(self):
        try:
            signer = Signature(self.sig_algo)
            public_key = signer.generate_keypair()[0]
            secret_key = signer.generate_keypair()[1]  # Never log secrets
            return public_key, secret_key
        except Exception as e:
            logging.error(f"Key generation failed: {str(e)}")
            raise

    def sign_message(self, message, secret_key):
        try:
            signer = Signature(self.sig_algo)
            return signer.sign(message, secret_key)
        except Exception as e:
            logging.error(f"Signing failed: {str(e)}")
            raise

    def verify_signature(self, message, signature, public_key=None):
        try:
            if not public_key:
                public_key = self._load_public_key()  # Assume stored public key
            signer = Signature(self.sig_algo)
            return signer.verify(message, signature, public_key)
        except Exception as e:
            logging.error(f"Verification failed: {str(e)}")
            return False

    def _load_public_key(self):
        # Simulate loading from secure vault; in prod, use env-agnostic vault
        if os.path.exists("public_key.bin"):
            with open("public_key.bin", 'rb') as f:
                return f.read()
        raise FileNotFoundError("Public key missing")

    # Secrets management: No exposure; rotation via external procedure

# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.