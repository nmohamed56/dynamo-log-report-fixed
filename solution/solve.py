#!/usr/bin/env python3

import json
import re
from collections import Counter
from pathlib import Path

LOG_PATH = Path("/app/access.log")
REPORT_PATH = Path("/app/report.json")
REQUEST_RE = re.compile(r'"[A-Z]+\s+(\S+)\s+HTTP/\d(?:\.\d)?"')


def main() -> None:
    path_counts: Counter[str] = Counter()
    first_seen: dict[str, int] = {}
    unique_ips: set[str] = set()
    total_requests = 0

    with LOG_PATH.open("r", encoding="utf-8") as log_file:
        for line_number, raw_line in enumerate(log_file):
            line = raw_line.strip()
            if not line:
                continue

            fields = line.split()
            if not fields:
                continue

            total_requests += 1
            unique_ips.add(fields[0])

            request_match = REQUEST_RE.search(line)
            if request_match is None:
                raise ValueError(f"Malformed request line at input line {line_number + 1}")

            path = request_match.group(1)
            if path not in first_seen:
                first_seen[path] = total_requests
            path_counts[path] += 1

    if total_requests == 0 or not path_counts:
        raise ValueError("The access log contains no request records")

    top_path = min(
        path_counts,
        key=lambda path: (-path_counts[path], first_seen[path]),
    )

    report = {
        "total_requests": total_requests,
        "unique_ips": len(unique_ips),
        "top_path": top_path,
    }

    with REPORT_PATH.open("w", encoding="utf-8") as report_file:
        json.dump(report, report_file, sort_keys=True)
        report_file.write("\n")


if __name__ == "__main__":
    main()
