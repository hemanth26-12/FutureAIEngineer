from parser import parse_log_line
from json_manager import add_log, load_logs, save_logs
from report import print_summary


def search_by_severity(severity: str):
    logs = load_logs()
    matches = [log for log in logs if log.severity.upper() == severity.upper()]
    if not matches:
        print("No matching logs found.")
        return

    print(f"\nLogs with severity {severity.upper()}:")
    for log in matches:
        print(f"[{log.timestamp}] {log.severity} - {log.message}")


def main():
    while True:
        print("\n1. Add log")
        print("2. Search by severity")
        print("3. Print summary")
        print("4. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            line = input("Enter log line: ")
            try:
                log = parse_log_line(line)
                add_log(log)
                print("Log added successfully.")
            except ValueError as exc:
                print(f"Error: {exc}")
        elif choice == "2":
            severity = input("Enter severity (HIGH/MEDIUM/LOW): ").strip()
            search_by_severity(severity)
        elif choice == "3":
            print_summary(load_logs())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
