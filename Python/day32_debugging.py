class AgeError(Exception):
    pass
try:

    age = int(input("Age: "))

    if age < 18:
        raise AgeError("Age must be at least 18.")
except AgeError as e:
    print(e)
else:
    print("Eligible")

    '''the error was at in if statement was not
      kept colon at the end of the statement and 
      exception was not defined also not 
      defined try and else blocks'''