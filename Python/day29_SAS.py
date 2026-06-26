def Attendance():
    attendance = [90,85,95,80,100]

    avg = sum(attendance)/len(attendance)
    
    print("Highest :",max(attendance))
    print("Lowest :",min(attendance))
    print("Avg :",avg)


Attendance()