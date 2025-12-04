# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.

import argparse
from .control_plane import PolicyEngine
from .agent_layer import AgentFederation, sample_task
from .orchestration import Orchestrator
from .monetization import MonetizationService
import logging

def main():
    parser = argparse.ArgumentParser(description="AetherForge CLI")
    parser.add_argument("--run-agents", action="store_true")
    parser.add_argument("--deploy", type=str, default="kubernetes")
    parser.add_argument("--payment", type=float, default=0.0)
    parser.add_argument("--tier", type=str, default="Free")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    policy = PolicyEngine()
    if not policy.enforce_policy("CLI_EXEC", args.tier):
        print("License enforcement failed. Acquire license.")
        return

    if args.run_agents:
        agents = AgentFederation()
        results = [agents.execute_task(sample_task, (i,), args.tier) for i in range(4)]
        print(f"Agent results: {results}")

    if args.payment > 0:
        mono = MonetizationService()
        receipt = mono.process_payment(args.payment, args.tier)
        print(f"Payment receipt: {receipt}")

    orch = Orchestrator()
    print(orch.simulate_deploy(args.deploy))

if __name__ == "__main__":
    main()

# Copyright © 2025 Devin B. Royal.
# All Rights Reserved.