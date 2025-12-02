#UI → PlayerManager → PlayerRepository → PlayerIO → CSV

from main.logic.playermanager import PlayerManager

class PlayerUI:
    def __init__(self):
        self.pm = PlayerManager()

    def register_player_ui(self):
        print("=== Register New Player ===")

        name = input("Name: ")
        dob = input("DOB (YYYY-MM-DD): ")
        address = input("Address: ")
        phone = input("Phone: ")
        email = input("Email: ")
        url = input("URL: ")
        username = input("Username (handle): ")
        team = input("Team: ")

        # TODO It registers player even if you enter nothing as an input
        try:
            self.pm.register_player(
                name, dob, address, phone, email, url, username, team
            )
            print("\nPlayer successfully registered!")
        except ValueError as e:
            print("\nError:", e)