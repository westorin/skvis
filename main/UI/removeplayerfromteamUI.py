class RemovePlayerfromTeamUI:
    def __init__(self, team_manager, current_user):
        self.team_manager = team_manager
        self.current_user = current_user

    def remove_player_from_team(self):
        print("\n--- Remove Player from Team ---")
        team_name = input("Enter the team name: ")
        player_handle = input("Enter the player's username to remove: ")

        try:
            team = self.team_manager.remove_player_from_team(
                self.current_user, team_name, player_handle
            )
            print(f"Player '{player_handle}' has been removed from team '{team_name}'.")
        except ValueError as e:
            print(f"Error: {e}")
        except PermissionError as e:
            print(f"Permission Error: {e}")

if __name__ == "__main__":
    from main.logic.teammanager import TeamManager
    from main.models.playermodel import Player

    current_user = Player(
        player_id=0,
        name="Admin",
        dob="",
        address="",
        phone="",
        email="",
        url="",
        username="admin",
        team="",
        role="admin"
    )
    team_manager = TeamManager()
    ui = RemovePlayerfromTeamUI(team_manager, current_user)
    ui.remove_player_from_team()