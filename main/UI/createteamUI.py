from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

'''
To run the main UI type this into terminal: 

python3 -m main.UI.createteamUI
'''

class CreateTeamUI:
    def __init__(self) -> None:
        data = DataWrapper()
        logic = LogicWrapper(data)
        self.tm = logic.team_manager

    def add_team_ui(self) -> None:
        print("Create a New Team")

        name = input("Team Name: ")
        captain = input("Captain Name: ")
        website_url = input("Website URL (optional): ")

        try:
            team = self.tm.register_team(
                name=name,
                captain_handle=captain,
                website_url=website_url
            )
            print(f"Team '{team.name}' created successfully!")
        except ValueError as e:
            print("Error:", e)


if __name__ == "__main__":
    ui = CreateTeamUI()
    ui.add_team_ui()