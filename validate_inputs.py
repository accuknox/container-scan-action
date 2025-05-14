import os
import sys

REQUIRED_FIELDS = [
    "ENDPOINT",
    "TOKEN",
    "TENANT_ID",
    "IMAGE",
    "TAG",
    "LABEL",
]

SEVERITY_LEVELS = {"UNKNOWN", "LOW", "MEDIUM", "HIGH", "CRITICAL"}
EXIT_CODES = {"0", "1"}


def exit_with_error(msg):
    print(f"[ERROR] {msg}")
    sys.exit(1)


def validate_required_fields():
    for field in REQUIRED_FIELDS:
        value = os.getenv(field)
        if not value:
            exit_with_error(f"Missing required input: {field}")


def validate_severity():
    severity = os.getenv("SEVERITY", "")
    if severity:
        levels = {s.strip().upper() for s in severity.split(",")}
        invalid = levels - SEVERITY_LEVELS
        if invalid:
            exit_with_error(f"Invalid severity level(s): {', '.join(invalid)}. Allowed: {', '.join(SEVERITY_LEVELS)}")


def validate_exit_code():
    code = os.getenv("CODE", "0")
    if code not in EXIT_CODES:
        exit_with_error(f"Invalid exit_code: {code}. Allowed values are: 0 or 1")


def validate_ignore_unfixed():
    value = os.getenv("IGNORE_UNFIXED", "false").lower()
    if value not in {"true", "false"}:
        exit_with_error("IGNORE_UNFIXED must be either 'true' or 'false'")


if __name__ == "__main__":
    validate_required_fields()
    validate_severity()
    validate_exit_code()
    validate_ignore_unfixed()
    print("[INFO] All inputs are valid.")

