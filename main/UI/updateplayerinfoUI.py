from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

class UpdatePlayerInfoUI:
    def __init__(self):
        data = DataWrapper()
        logic = LogicWrapper(data)
        self.player_manager = logic.player_manager
        
    def ui(self):
        print("=== Update Player Information ===")

        player_username = input("Enter Player username to update: ").strip()

        print("\nWhat do you want to update?")
        print("1. Name")
        print("2. Date of Birth")
        print("3. Address")
        print("4. Phone")
        print("5. Email")
        print("6. URL")
        print("7. Username")
        print("8. Team")

        choice = input("Enter choice (1-8): ").strip()
        field_map = {
            "1": "name",
            "2": "dob",
            "3": "address",
            "4": "phone",
            "5": "email",
            "6": "url",
            "7": "username",
            "8": "team"
        }

        if choice == "9":
            print("Update cancelled.")
            return
        
        if choice not in field_map:
            print("Invalid choice. Update cancelled.")
            return
        
        field = field_map[choice]
        new_value = input(f"Enter new value for {field}: ").strip()


        try:
            updated_player = self.player_manager.update_player(
                player_username,
                **{field: new_value}
            )
            print(f"Player '{player_username}' updated successfully.")
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    UpdatePlayerInfoUI().ui()
