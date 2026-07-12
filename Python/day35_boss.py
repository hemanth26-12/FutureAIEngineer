import sys

class Asset:
    def __init__(self, Asset_ID, Name, Emp, Status, FileName = "assets.txt"):
        self.Asset_ID = Asset_ID
        self.Name = Name
        self.Emp = Emp
        self.Status = Status
        self.FileName = FileName

    def display(self):
        print("Asset Id:", self.Asset_ID)
        print("Name :", self.Name)
        print("Employee :", self.Emp)
        print("Status :", self.Status)


def find_asset_by_id(asset_list, asset_id):
    for asset in asset_list:
        if asset.Asset_ID == asset_id:
            return asset
    return None


def find_asset_by_name(asset_list, asset_name):
    search_name = asset_name.strip().lower()
    for asset in asset_list:
        if asset.Name.lower() == search_name:
            return asset
    return None


def save_assets(asset_list):
    for asset in asset_list:
        with open(asset.FileName, "a+") as f:
            entry = f"{asset.Asset_ID}|{asset.Name}|{asset.Emp}|{asset.Status}\n"
            f.write(entry)


def display_assets(asset_list):
    for asset in asset_list:
        asset.display()
        print("_" * 30)


def get_search_input():
    if len(sys.argv) > 2:
        search_type = sys.argv[1].lower()
        search_value = sys.argv[2]
        return search_type, search_value

    search_type = input("Search by ID or Name? (id/name): ").strip().lower()
    if search_type not in {"id", "name"}:
        print("Please enter 'id' or 'name'.")
        return None, None

    search_value = input("Enter search value: ").strip()
    return search_type, search_value


assets = [
    Asset(121, "Hemanth", "emp121", "Online"),
    Asset(123, "Ravi", "emp123", "Offline"),
    Asset(124, "Ramu", "emp124", "NotAvailable")
]

save_assets(assets)
display_assets(assets)

search_type, search_value = get_search_input()
if search_type == "id":
    try:
        search_id = int(search_value)
    except (TypeError, ValueError):
        print("Invalid ID. Please enter a numeric Asset ID.")
    else:
        found = find_asset_by_id(assets, search_id)
        if found:
            print("\nAsset found:")
            found.display()
        else:
            print("\nAsset not found.")
elif search_type == "name":
    found = find_asset_by_name(assets, search_value)
    if found:
        print("\nAsset found:")
        found.display()
    else:
        print("\nAsset not found.")
