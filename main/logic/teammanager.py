from main.models.teammodel import Team

class TeamManager:
    def __init__(self, team_repo=None, player_repo=None):
        self.team_repo = team_repo
        self.player_repo = player_repo

    # Create a new team ============================
    def register_team(self, name, captain_handle, website_url="") -> "Team":
        team_id = self.team_repo.get_next_id()

        # Look up captain by name
        captain = self.player_repo.get_by_handle(captain_handle)
        if captain is None:
            print("DEBUG PLAYERS:", [(p.username) for p in self.player_repo.players])
            raise ValueError("Captain must be a registered player")
            

        # Team name must be unique
        if self.team_repo.get_team(name):
            raise ValueError("Team name must be unique")

        new_team = Team(
            team_id=team_id,
            name=name,
            captain=captain_handle,
            players=[captain_handle],
            website_url=website_url
        )

        # Add team to repository
        self.team_repo.add_team(new_team)

        # Assign captain to the team
        captain.team = name
        self.player_repo.save_players()

        return new_team

    # Add a player to a team ============================ 
    def add_player_to_team(self, team_name, player_handle):
        team = self.team_repo.get_team(team_name)
        if team is None:
            raise ValueError("Team does not exist")

        # Look up player object by name
        player = self.player_repo.get_by_handle(player_handle)
        if player is None:
            raise ValueError("Player does not exist")

        if player.team == team_name:
            raise ValueError("Player is already in the team")

        # Max team size = 5
        if len(team.players) >= 5:
            print("DEBUG team.players =", team.players, type(team.players))
            raise ValueError("Team is already full (max 5 players)")

        # Add player to team
        team.players.append(player_handle)
        player.team = team_name

        # Save updates
        self.team_repo.save_teams()
        self.player_repo.save_players()

        return team
    
    # Remove a player from a team ===========================
    def remove_player_from_team(self, current_user, team_name, player_handle):
        team = self.team_repo.get_team(team_name)
        # If team does not exist, raise error
        if not team:
            raise ValueError("Team does not exist")

        player = self.player_repo.get_by_handle(player_handle)
        # If player does not exist, raise error
        if not player: 
            raise ValueError("Player does not exist")
        
        #Permission check
        if current_user.role == "captain":
            raise PermissionError("Captains can only edit their own team")
        elif current_user.role == "player":
            raise PermissionError("Players cannot remove other players")
        
        # Check if player is in the team
        if player_handle not in team.players:
            raise ValueError("Player is not in the team")
        
        # Do NOT allow removing captain unless by admin
        if player_handle == team.captain and current_user.role != "admin":
            raise ValueError("Cannot remove the team captain unless you are an admin")
        
        # Remove player from team
        team.players.remove(player_handle)

        #Update player's team to empty
        player.team = ""

        #Save updates
        self.team_repo.save_teams()
        self.player_repo.save_players()

        return team

    # Sync team assignment when updating player's team ===========================
    def update_player_team(self, player_handle, new_team):
        # If new_team is a Team object, convert it to its name
        if hasattr(new_team, "name"):
            new_team = new_team.name

        # If no new team was provided, do nothing
        if not new_team or new_team.strip() == "":
            return

        # Load player to check current team
        player = self.player_repo.get_by_handle(player_handle)
        if not player:
            raise ValueError("Player does not exist")

        # If updating username triggers this function by mistake, ignore it
        # (username == new_team -> invalid)
        if new_team == player_handle:
            return

        # If player is already in the correct team, nothing to do
        if player.team == new_team:
            return

        # Remove player from old team
        for team in self.team_repo.teams:
            if player_handle in team.players:
                team.players.remove(player_handle)
                break

        # Add to new team ONLY if it exists
        new_team_obj = self.team_repo.get_team(new_team)
        if new_team_obj is None:
            raise ValueError("New team does not exist")

        new_team_obj.players.append(player_handle)

        # Update player CSV team
        player.team = new_team
        self.player_repo.save_players()

        # Save updated teams
        self.team_repo.save_teams()


    # Sync username changes inside team players list ===========================
    def update_username_in_teams(self, old_handle, new_handle):
        # Replace old username with new username in every team
        for team in self.team_repo.teams:
            team.players = [
                new_handle if p == old_handle else p
                for p in team.players
            ]

            # Update captain field if needed
            if team.captain == old_handle:
                team.captain = new_handle

        # Save updated teams
        self.team_repo.save_teams()

    # Get all teams ===========================
    def get_all_teams(self):
        return self.team_repo.teams
    
    def get_team(self, team_name):
        return self.team_repo.get_team(team_name)
