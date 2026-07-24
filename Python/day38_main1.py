import json_manager
import day38_search
def load_applications():
    return json_manager.load_applications()
def save_applications(applications):
    json_manager.save_applications(applications)
def add_application():
    company = input("Enter company: ").strip()
    role = input("Enter role: ").strip()
    status = input("Enter status: ").strip()
    experience_input = input("Enter experience (years): ").strip()
    try:
        experience = int(experience_input)
    except ValueError:
        print("Experience must be a number.")
        return
    json_manager.add_application(company, role, status, experience)
    print("Application saved successfully.")
def main():
    while True:
        print("\n1) Add Application")
        print("2) Search Applications")
        print("3) Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_application()
        elif choice == "2":
            day38_search.search()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()