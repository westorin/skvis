from main.logic.teammanager import TeamManager

class AddTeamUI:
    def __init__(self) -> None:
        self.at = TeamManager()

    def add_team_ui(self) -> None:
        print("=== Create a new team ===")

        name = input("Name: ")
        captain = input("Captain: ")
        players = input(" ") # Spurning hvernig þetta á að vera
        website_url = input("URL: ")

        data = {
            "name": name,
            "captain": captain,
            "players": players,
            "website_url" = website_url,
        }

        try:
            self.at.add_team(data)
            print("Team successfully created!")
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    ui = AddTeamUI()
    ui.add_team_ui()