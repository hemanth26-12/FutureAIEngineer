import json
from pathlib import Path
from day38_application import Application

DATA_FILE = Path(__file__).with_name("application.json")


def load_applications():
    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            records = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Invalid JSON in application data.")
        return []

    applications = []
    for item in records:
        if isinstance(item, dict):
            applications.append(Application.from_dict(item))
    return applications


def save_applications(applications):
    with DATA_FILE.open("w", encoding="utf-8") as file:
        json.dump([app.to_dict() for app in applications], file, indent=4)


def add_application(company, role, status, experience):
    new_app = Application(company, role, status, experience)
    applications = load_applications()
    applications.append(new_app)
    save_applications(applications)
    return new_app


def search_applications(keyword):
    keyword = keyword.strip().lower()
    if not keyword:
        return []

    applications = load_applications()
    return [
        app
        for app in applications
        if keyword in app.Company.lower()
        or keyword in app.Role.lower()
        or keyword in app.Status.lower()
    ]
