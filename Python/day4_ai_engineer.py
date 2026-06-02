Name = input("Enter your name: ")
Python_Skill = int(input("Rate your Python skill (1-10): "))
DSA_Skill = int(input("Rate your DSA skill (1-10): "))
AI_Interest = input("Are you interested in AI? (yes/no): ")
if Python_Skill >= 7 and DSA_Skill >= 5 and AI_Interest.lower() == "yes":
    print("AI Engineer Path Recommended")
else:
    print("Improve Your Skills")