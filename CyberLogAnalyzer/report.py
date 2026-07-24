from collections import Counter
from typing import List
from log import LogEntry


def generate_summary(logs: List[LogEntry]) -> dict:
    severity_counts = Counter(log.severity for log in logs)
    return {
        "total_logs": len(logs),
        "severity_counts": dict(severity_counts),
    }


def print_summary(logs: List[LogEntry]) -> None:
    summary = generate_summary(logs)
    print("\n=== Security Log Summary ===")
    print(f"Total logs: {summary['total_logs']}")
    for severity, count in summary["severity_counts"].items():
        print(f"{severity}: {count}")
