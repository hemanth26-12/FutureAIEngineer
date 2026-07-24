from log import LogEntry


def parse_log_line(line: str) -> LogEntry:
    parts = line.strip().split(" ", 3)
    if len(parts) < 4:
        raise ValueError("Invalid log format")

    timestamp = parts[0] + " " + parts[1]
    severity = parts[2].upper()
    message = parts[3]
    return LogEntry(timestamp=timestamp, severity=severity, message=message)
