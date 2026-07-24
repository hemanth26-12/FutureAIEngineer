import json

student = {
    "name": "Hemanth",
    "age": 20,
    "course": "AI Engineering",
    "year": 2,
    "grades": {
        "math": 95,
        "python": 98,
        "ai": 97
    }
}

with open("student.json", "w") as f:
    json.dump(student, f, indent=4)

with open("student.json", "r") as f:
    data = json.load(f)

print(data)

