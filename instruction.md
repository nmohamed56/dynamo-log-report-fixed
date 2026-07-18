# Access log report

Analyze the Apache-style access log at `/app/access.log` and create `/app/report.json`.

## Success criteria

1. `/app/report.json` exists and is valid UTF-8 JSON. Its top-level value is an object containing exactly the keys `total_requests`, `unique_ips`, and `top_path`.
2. `total_requests` is the integer `6`, equal to the number of non-empty request lines in `/app/access.log`.
3. `unique_ips` is the integer `3`, equal to the number of distinct client IP addresses in the first whitespace-delimited field of the log lines.
4. `top_path` is the string `"/index.html"`, equal to the request target that occurs most often inside the quoted HTTP request lines.
