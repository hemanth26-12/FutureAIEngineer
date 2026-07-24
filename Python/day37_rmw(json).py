import json
data = [
    {
        "empid 1": "101D",
        "empname": "Hemanth",
        "department": "technical",
        "company": "amazon"
    },
    {
        "empid 2": "102D",
        "empname": "Herine",
        "department": "it",
        "company": "flipkart"
    },
    {
        "empid 3": "103D",
        "empname": "harry",
        "department": "tester",
        "company": "amazon"
    }
]

with open("employees.json", "w+") as f:
    json.dump(data,f,indent = 4)

with open("employees.json","r")as f:
    v = json.load(f)

print(v)