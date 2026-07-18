import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")
EXPECTED_KEYS = {"total_requests", "unique_ips", "top_path"}


def load_report():
    return json.loads(REPORT_PATH.read_text(encoding="utf-8"))


def test_success_criterion_1_report_is_exact_json_object():
    """Success criterion 1: report.json is UTF-8 JSON with exactly the required keys."""
    assert REPORT_PATH.is_file(), "/app/report.json does not exist"
    report = load_report()
    assert type(report) is dict, "the top-level JSON value must be an object"
    assert set(report) == EXPECTED_KEYS, (
        f"expected exactly keys {sorted(EXPECTED_KEYS)}, got {sorted(report)}"
    )


def test_success_criterion_2_total_requests():
    """Success criterion 2: total_requests is the integer 6."""
    report = load_report()
    assert type(report["total_requests"]) is int, "total_requests must be an integer"
    assert report["total_requests"] == 6


def test_success_criterion_3_unique_ips():
    """Success criterion 3: unique_ips is the integer 3."""
    report = load_report()
    assert type(report["unique_ips"]) is int, "unique_ips must be an integer"
    assert report["unique_ips"] == 3


def test_success_criterion_4_top_path():
    """Success criterion 4: top_path is the string /index.html."""
    report = load_report()
    assert type(report["top_path"]) is str, "top_path must be a string"
    assert report["top_path"] == "/index.html"
