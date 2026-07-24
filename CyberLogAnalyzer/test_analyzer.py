import os
import sys
import tempfile
import unittest

sys.path.insert(0, os.path.dirname(__file__))

from json_manager import load_logs, save_logs
from log import LogEntry
from parser import parse_log_line
from report import generate_summary


class AnalyzerTests(unittest.TestCase):
    def test_parse_and_persist_logs(self):
        log = parse_log_line("2026-07-20 10:15:00 HIGH Login failed for user admin")
        self.assertIsInstance(log, LogEntry)
        self.assertEqual(log.severity, "HIGH")
        self.assertIn("Login", log.message)

        with tempfile.TemporaryDirectory() as tmpdir:
            path = os.path.join(tmpdir, "logs.json")
            save_logs([log], path)
            loaded = load_logs(path)
            self.assertEqual(len(loaded), 1)
            self.assertEqual(loaded[0].severity, "HIGH")

    def test_generate_summary(self):
        logs = [
            LogEntry("2026-07-20 10:00:00", "HIGH", "Firewall blocked attack"),
            LogEntry("2026-07-20 10:05:00", "MEDIUM", "Suspicious login"),
            LogEntry("2026-07-20 10:10:00", "LOW", "User logged in"),
        ]
        summary = generate_summary(logs)
        self.assertEqual(summary["total_logs"], 3)
        self.assertEqual(summary["severity_counts"]["HIGH"], 1)


if __name__ == "__main__":
    unittest.main()
