def Skill_Tracker():

    skills = [
        "Python",
        "AI",
        "ML",
        "Cybersecurity"
    ]
    print(f"Total Skills: {len(skills)}")
    print()
    for i, skill in enumerate(skills, 1):
        print(f"{i}. {skill}")


e1 = Skill_Tracker()
