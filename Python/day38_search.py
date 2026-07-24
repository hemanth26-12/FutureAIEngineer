import json_manager


def search():
    keyword = input("Enter name to search: ").strip()
    if not keyword:
        print("Search term cannot be empty.")
        return

    matches = json_manager.search_applications(keyword)

    if not matches:
        print("No matching applications found.")
        return

    print("\nSearch Results:")
    for app in matches:
        print(f"Company: {app.Company}")
        print(f"Role: {app.Role}")
        print(f"Status: {app.Status}")
        print(f"Experience: {app.Experience}")
        print("-" * 30)


if __name__ == "__main__":
    search()

