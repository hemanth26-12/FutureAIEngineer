applications = [
    {
        "Company":"Amazon",
        "Role":"HR",
        "Stipend":15000,
        "Status":"Applied"
    },
    {
        "Company":"Flipkart",
        "Role":"HR",
        "Stipend":10000,
        "Status":"Not Applied"
    },
    {
        "Company":"Wipro",
        "Role":"Manager",
        "Stipend":15000,
        "Status":"Progressing"
    }
]


with open("internships.txt","a+") as f:
    for items in applications:
     f.write(f"Company: {items["Company"]}\n")
     f.write(f"Role: {items["Role"]}\n")
     f.write(f"Stipend: {items["Stipend"]}\n")
     f.write(f"Status: {items["Status"]}\n")
     f.write("\n")

