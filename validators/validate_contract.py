#!/usr/bin/env python3

"""MSCE Memory Contract v1 validator."""

from __future__ import annotations

import json
import sys
from datetime import datetime
from pathlib import Path

try:
    from jsonschema import Draft202012Validator, FormatChecker
    from jsonschema.exceptions import ValidationError
except ImportError:
    print("Missing dependency: jsonschema")
    sys.exit(1)


ROOT = Path(__file__).resolve().parents[1]
SCHEMA = ROOT / "schema" / "msce-memory-contract-v1.json"


def validate_payload(payload_path: Path) -> bool:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    payload = json.loads(payload_path.read_text(encoding="utf-8"))

    try:
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        validator.validate(payload)

        datetime.fromisoformat(
            payload["timestamp"].replace("Z", "+00:00")
        )

    except (ValidationError, ValueError, KeyError) as exc:
        print("INVALID")
        print(str(exc))
        return False

    print("VALID")
    return True


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: validate_contract.py <payload.json>")
        return 1

    return 0 if validate_payload(Path(sys.argv[1])) else 1


if __name__ == "__main__":
    raise SystemExit(main())
