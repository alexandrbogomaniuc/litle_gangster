#!/usr/bin/env python3
"""Create a machine-readable manifest for a non-production visual sandbox."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def safe_slug(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9_-]+", "_", value.strip()).strip("_").lower()
    return slug or "visual"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", type=Path, required=True)
    parser.add_argument("--game-id", required=True)
    parser.add_argument("--slug", required=True)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    project_root = args.project_root.resolve()
    slug = safe_slug(args.slug)
    sandbox_path = project_root / "11_prototypes" / f"{args.game_id}_{slug}_visual_sandbox"
    manifest = {
        "gameId": str(args.game_id),
        "slug": slug,
        "sandboxPath": str(sandbox_path),
        "nonProduction": True,
        "donorAssetsPlaceholderOnly": True,
        "productionAssetsCreated": False,
        "productionClientCodeGenerated": False,
        "gsCallsEnabled": False,
        "walletCallsEnabled": False,
        "externalCallsEnabled": False,
        "releaseAllowed": False,
    }

    text = json.dumps(manifest, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(text, encoding="utf-8")
    else:
        print(text, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
