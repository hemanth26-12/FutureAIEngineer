with open("expenses.txt","w+") as f:
    f.write(input("Expenses Name: \n"))
    f.write(input("Amount: \n"))

    f.seek(0)
    print(f.read())