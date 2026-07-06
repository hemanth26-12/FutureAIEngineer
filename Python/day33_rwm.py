def add_application():
    """Add a new job application entry"""
    with open("applications.txt", "a") as f:
        company = input("Enter Company Name: ")
        role = input("Enter Role: ")
        date_applied = input("Enter Date Applied (DD/MM/YYYY): ")
        status = input("Enter Status (Applied/Rejected/Interview/Accepted): ")
        
        # Format and write to file
        entry = f"{company}|{role}|{date_applied}|{status}\n"
        f.write(entry)
        print("✓ Application added successfully!\n")

def display_applications():
    """Display all job applications"""
    try:
        with open("applications.txt", "r") as f:
            applications = f.readlines()
            
        if not applications:
            print("No applications recorded yet.\n")
            return
        
        print("\n" + "="*80)
        print(f"{'Company':<20} {'Role':<20} {'Date Applied':<15} {'Status':<15}")
        print("="*80)
        
        for app in applications:
            company, role, date_applied, status = app.strip().split("|")
            print(f"{company:<20} {role:<20} {date_applied:<15} {status:<15}")
        print("="*80 + "\n")
        
    except FileNotFoundError:
        print("No applications file found yet.\n")

def menu():
    """Main menu"""
    while True:
        print("Job Application Tracker")
        print("-" * 40)
        print("1. Add New Application")
        print("2. Display All Applications")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == "1":
            add_application()
        elif choice == "2":
            display_applications()
        elif choice == "3":
            print("Thank you for using Job Application Tracker!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
if __name__ == "__main__":
    menu()
