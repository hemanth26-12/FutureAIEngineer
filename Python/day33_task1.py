with open("student1.txt","w+") as f:
    f.write("Name: Hemanth\n" 
    "Branch: CSM\n"
    "Year :3RD YEAR")
    f.seek(0)
    c=f.read()
    print(c)
