from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

'''
To run the main UI type this into terminal: 

python3 -m main.UI.addplayertoteamUI 
'''

class AddPlayerToTeamUI:
    def __init__(self) -> None:
        data = DataWrapper()
        logic = LogicWrapper(data)
        self.tm = logic.team_manager

    def add_player_ui(self) -> None:
        print("Add Player to a Team")

        team_name = input("Team name: ")
        player_handle = input("Player handle: ")

        try:
            team = self.tm.add_player_to_team(team_name, player_handle)
            print(f"\nPlayer {player_handle} added to team {team_name} successfully.")
        except ValueError as e:
            print("\nError:",e)

if __name__ == "__main__":
    AddPlayerToTeamUI().add_player_ui()
