#!/usr/bin/env python3

"""MSCE Memory Contract v1 validator."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from jsonschema import validate
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
        validate(instance=payload, schema=schema)
    except ValidationError as exc:
        print("INVALID")
        print(exc.message)
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
