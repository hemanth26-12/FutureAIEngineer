from dataclasses import dataclass


@dataclass
class LogEntry:
    timestamp: str
    severity: str
    message: str

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "severity": self.severity,
            "message": self.message,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            timestamp=data.get("timestamp", ""),
            severity=data.get("severity", "UNKNOWN"),
            message=data.get("message", ""),
        )
