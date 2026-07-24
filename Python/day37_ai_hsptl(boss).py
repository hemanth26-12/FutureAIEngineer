import json
import os
FILE_PATH = os.path.join(os.path.dirname(__file__), "patient.json")
def load_patients():
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as file:
            return json.load(file)
    return []
def save_patients(patients):
    with open(FILE_PATH, "w") as file:
        json.dump(patients, file, indent=4)
def search_patient(patients, query):
    query = query.lower()
    for patient in patients:
        if query in str(patient["ID"]).lower() or query in patient["Name"].lower():
            return patient
    return None
def update_bill(patients, patient_id, new_bill):
    for patient in patients:
        if patient["ID"] == patient_id:
            patient["Bill"] = new_bill
            return True
    return False
def display_patients(patients):
    if not patients:
        print("No patient records found.")
        return
    for patient in patients:
        print(
            f"ID: {patient['ID']}, Name: {patient['Name']}, Age: {patient['Age']}, "
            f"Disease: {patient['Disease']}, Doctor: {patient['Doctor']}, Bill: {patient['Bill']}"
        )
def main():
    patients = load_patients()
    if not patients:
        patients = [
            {
                "ID": "101D",
                "Name": "Hemanth",
                "Age": 19,
                "Disease": "Sighness",
                "Doctor": "ramarao",
                "Bill": "4000/-",
            },
            {
                "ID": "102D",
                "Name": "Harry",
                "Age": 20,
                "Disease": "Cough",
                "Doctor": "ramarao",
                "Bill": "2000/-",
            },
            {
                "ID": "103D",
                "Name": "Minna",
                "Age": 26,
                "Disease": "Sighness",
                "Doctor": "ramu",
                "Bill": "4000/-",
            },
        ]
        save_patients(patients)

    print("AI Hospital Database")
    display_patients(patients)

    while True:
        print("\n1. Search Patient")
        print("2. Update Bill")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            query = input("Enter patient ID or name: ")
            patient = search_patient(patients, query)
            if patient:
                print("Patient found:", patient)
            else:
                print("Patient not found.")

        elif choice == "2":
            patient_id = input("Enter patient ID: ")
            new_bill = input("Enter new bill: ")
            if update_bill(patients, patient_id, new_bill):
                save_patients(patients)
                print("Bill updated successfully.")
            else:
                print("Patient not found.")

        elif choice == "3":
            break

        else:
            print("Invalid choice.")

    print("\nFinal patient records:")
    display_patients(patients)
if __name__ == "__main__":
    main()


