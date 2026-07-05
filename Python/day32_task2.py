class InsufficientBalanceError(Exception):
    pass

try:
    Balance = float(input("Enter your account balance: "))
    WithdrawalAmount = float(input("Enter the amount to withdraw: "))

    if WithdrawalAmount > Balance:
        raise InsufficientBalanceError("Insufficient balance for the withdrawal.")
except InsufficientBalanceError as e:
    print(e)
else:
    print("Withdrawal Successful")
    print("Remaining Balance:", Balance - WithdrawalAmount)