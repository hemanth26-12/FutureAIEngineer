skills = {
    "Python": 80,
    "AI": 60,
    "Ml": 50,
    "Cybersecurity": 40
}

def show_skills(skills):
    for skill, percent in skills.items():
        print(skill, ":", str(percent) + "%")

show_skills(skills)
