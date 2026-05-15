#!/usr/bin/env python3
"""Generate a safe prompt for a parallel math validation thread or subagent."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


def load_request(path: str | None) -> dict:
    if not path:
        return {}
    if path == "-":
        text = sys.stdin.read()
    else:
        text = Path(path).read_text(encoding="utf-8")
    return json.loads(text) if text.strip() else {}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--request", help="JSON request file, or '-' for stdin")
    parser.add_argument("--output-folder", required=True)
    parser.add_argument("--game-key", default="generic-game")
    args = parser.parse_args()

    request = load_request(args.request)
    scope = request.get("simulationScope") or request.get("simulation_scope") or "declare train/validation/tail/bonus-buy/FRB scope"

    prompt = f"""You are running a parallel math validation lane for {args.game_key}.

Write only to this parallel output folder:
{args.output_folder}

Hard restrictions:
- no active config changes
- no validation-seed tuning
- no backend/client/registration/release actions
- no DB/Cassandra execution
- no wallet/API calls
- no donor browsing or asset capture
- no certification or release claim

Requested simulation scope:
{json.dumps(scope, sort_keys=True)}

Validate the 3x3 RTP/volatility matrix unless the request explicitly documents a smaller approved matrix. Use train seeds only for tuning. Use validation seeds only for validation. Use separate tail/max-win seed family for cap and max-win confidence. If bonus buy exists, report BF_RTP, BF_RTP_MIN, BF_BETS, cost denominator, purchased feature wins, cap behavior, and blockers. If FRB/promo exists, report promo EV, campaign liability, state/history behavior, settlement/accounting behavior, replay/VABS behavior, cap behavior, and blockers.

Produce machine-readable JSON plus a compact markdown report with:
- requestValid
- profilesExpectedCount
- profilesTestedCount
- trainGateStatus
- validationGateStatus
- tailMaxWinGateStatus
- bonusBuyGateStatus
- frbPromoGateStatus
- registrationFieldCandidates
- confidenceSummary
- exactValuesFinal=false unless separately approved
- certificationStatus=false unless separately approved
- unresolvedBlockers
"""
    print(prompt)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
