import json
from day38_application import Application

applications = [
    Application("Amazon", "HR", "Applied", 3),
    Application("Flipkart", "tester", "Not Applied", 3),
]

with open("application.json", "w", encoding="utf-8") as f:
    json.dump([app.to_dict() for app in applications], f, indent=4)

with open("application.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(data)