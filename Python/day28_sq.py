def Student():
    marks = [85, 92, 76, 88, 95]

    avg = sum(marks) / len(marks)
    print("Highest :", max(marks))
    print("Lowest :", min(marks))
    print("Average :", avg)

    if avg >= 90:
        grade = "A"
    elif avg >= 80:
        grade = "B"
    elif avg >= 70:
        grade = "C"
    else:
        grade = "D"

    print("Grade :", grade)

Student()

