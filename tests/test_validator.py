#!/usr/bin/env python3

"""MSCE-Contract v1 validation tests."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = ROOT / "validators" / "validate_contract.py"


def run_validator(path: Path) -> bool:
    result = subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        capture_output=True,
        text=True,
    )
    return result.returncode == 0


def main() -> int:
    tests = [
        (
            ROOT / "examples" / "completed-task.json",
            True,
        ),
        (
            ROOT / "tests" / "invalid_payloads" / "invalid-confidence.json",
            False,
        ),
        (
            ROOT / "tests" / "invalid_payloads" / "invalid-lifecycle.json",
            False,
        ),
        (
            ROOT / "tests" / "invalid_payloads" / "missing-provenance.json",
            False,
        ),
    ]

    failures = 0

    for payload, expected in tests:
        result = run_validator(payload)

        if result == expected:
            print(f"PASS: {payload.name}")
        else:
            print(f"FAIL: {payload.name}")
            failures += 1

    return failures


if __name__ == "__main__":
    raise SystemExit(main())
