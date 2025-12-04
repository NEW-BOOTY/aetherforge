# AetherForge Platform

## Overview
AetherForge is an original, governed, monetizable platform with runtime license enforcement, PQC security, and agent federation. Unique architecture: Modular control plane orchestrates isolated agents with policy gates.

## Build/Run Instructions
- Install Bazel, Python 3.12, liboqs-python (pip install liboqs-python), and other deps.
- bazel build //:aetherforge_cli
- bazel test //:aetherforge_test
- ./demo.sh

## Security Notes
- PQC: Kyber/Dilithium used; install liboqs-python.
- Secrets: Use vault; no hardcodes.
- Isolation: Multiprocessing; enhance with namespaces in prod.

## Deployment Tips
- Kubernetes: Use provided manifests (simulate in demo).
- Clouds: Dry-run in demo; adapt for real.

## Marketplace Readiness Checklist
- Packaging: Containerized artifacts.
- Metadata: See marketplace/ files.

Copyright © 2025 Devin B. Royal. All Rights Reserved.