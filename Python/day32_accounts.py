class InvalidUserError(Exception):
    pass

class WeakPasswordError(Exception):
    pass

class InvalidRoleError(Exception):
    pass


def validate_account(acc):
    errors = []
    if acc.get('role') not in ("Admin", "Security", "Operator"):
        errors.append(InvalidRoleError("Invalid role."))
    if len(acc.get('password', '')) < 8:
        errors.append(WeakPasswordError("Password must be atleast 8 characters long."))
    if acc.get('username', '') == "":
        errors.append(InvalidUserError("Invalid Username."))
    return errors


def main():
    # Five sample accounts demonstrating different errors
    accounts = [
        {'username': 'alice', 'password': 'securePass1', 'role': 'Admin'},   # valid
        {'username': 'bob', 'password': '12345', 'role': 'Admin'},           # weak password
        {'username': '', 'password': 'strongPass2', 'role': 'Operator'},    # invalid username
        {'username': 'carol', 'password': 'pwd', 'role': 'Guest'},          # weak password + invalid role
        {'username': 'dave', 'password': 'short', 'role': 'Visitor'},       # weak password + invalid role
    ]

    for i, acc in enumerate(accounts, start=1):
        print(f"Account {i}:")
        print("  Username:", acc.get('username'))
        print("  Role:", acc.get('role'))

        errs = validate_account(acc)
        if errs:
            print("  Errors:")
            for e in errs:
                print("   -", e)
        else:
            print("  Status: OK")

        print()


if __name__ == '__main__':
    main()
