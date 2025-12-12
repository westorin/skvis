from main.models.teammodel import Team
from main.models.passwordsmodel import PasswordsManager
from main.logic.listOfTeams import ListOfTeamsLogic
from typing import Optional, List, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from main.repo.teamrepo import TeamRepository
    from main.repo.playerrepo import PlayerRepository
    from main.repo.passwordrepo import PasswordRepository

class TeamManager:
    """Logic for creating and managing teams."""
    def __init__(self, team_repo: Optional["TeamRepository"] = None, player_repo: Optional["PlayerRepository"] = None, password_repo: Optional["PasswordRepository"] = None) -> None:
        self.team_repo = team_repo
        self.player_repo = player_repo
        self.password_repo = password_repo

    # Create a new team
    def register_team(self, name: str, captain_handle: str, website_url: str = "") -> Team:
        """Create a new team and assign a captain. Returns the created team."""
        team_id: int = self.team_repo.get_next_id()

        # Look up captain by name
        captain = self.player_repo.get_by_handle(captain_handle)
        if captain is None:
            raise ValueError("Captain must be a registered player.")
            
        # Team name must be unique
        if self.team_repo.get_team(name):
            raise ValueError("Team name must be unique.")

        new_team = Team(
            team_id=team_id,
            name=name,
            captain=captain_handle,
            players=[captain_handle],
            website_url=website_url,
            wins=0,
            losses=0
        )

        # Add team to repository
        self.team_repo.add_team(new_team)

        # Assign captain to the team
        captain.team = name
        self.player_repo.save_players()

        if self.password_repo.get_by_username(captain_handle) is None:
            pw = PasswordsManager(captain_handle, "captain123")
            self.password_repo.passwords.append(pw)
            self.password_repo.save_passwords()

        return new_team

    # Add player to a team
    def add_player_to_team(self, team_name: str, player_handle: str) -> Team:
        """Add a player to an existing team."""
        team = self.team_repo.get_team(team_name)
        if team is None:
            raise ValueError("Team does not exist.")

        # Look up player by handle
        player = self.player_repo.get_by_handle(player_handle)
        if player is None:
            raise ValueError("Player does not exist.")

        if player.team == team_name:
            raise ValueError("Player is already in the team.")

        # Max team size = 5
        if len(team.players) >= 5:
            raise ValueError("Team is already full (max 5 players).")

        # Add player to team
        team.players.append(player_handle)
        player.team = team_name

        # Save updates
        self.team_repo.save_teams()
        self.player_repo.save_players()

        return team
    
    # Remove a player from a team
    def remove_player_from_team(self, current_user: Any, team_name: str, player_handle: str) -> Team:
        """Remove player from a team."""
        team = self.team_repo.get_team(team_name)
        if not team:
            raise ValueError("Team does not exist.")

        player = self.player_repo.get_by_handle(player_handle)
        if not player: 
            raise ValueError("Player does not exist.")
        
        #Permission check
        if current_user.role == "captain":
            raise PermissionError("Captains can only edit their own team.")
        elif current_user.role == "player":
            raise PermissionError("Players cannot remove other players.")
        
        # Check if player is in the team
        if player_handle not in team.players:
            raise ValueError("Player is not in the team.")
        
        # Do NOT allow removing captain unless by admin
        if player_handle == team.captain and current_user.role != "admin":
            raise ValueError("Cannot remove the team captain unless you are an admin.")
        
        # Remove player from team
        team.players.remove(player_handle)
        player.team = ""

        # Save updates
        self.team_repo.save_teams()
        self.player_repo.save_players()

        return team

    # Sync team assignment when updating player's team
    def update_player_team(self, player_handle: str, new_team: Any) -> None:
        """Sync team membership when a player's team changes."""
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

        # Ignore accidental calls caused by username updates
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

        # Update player record
        player.team = new_team
        self.player_repo.save_players()

        # Save updated teams
        self.team_repo.save_teams()


    # Sync username changes inside team players list
    def update_username_in_teams(self, old_handle: str, new_handle: str) -> None:
        """Replace old username with new username in every team"""
        for team in self.team_repo.teams:
            team.players = [
                new_handle if p == old_handle else p
                for p in team.players
            ]

            # Update captain field if needed
            if team.captain == old_handle:
                team.captain = new_handle

        self.team_repo.save_teams()

    def get_team_by_captain(self, captain_handle: str) -> Optional[Team]:
        """Return the team where this username is captain or None."""
        for team in self.team_repo.teams:
            if team.captain == captain_handle:
                return team
        return None

    # Get all teams 
    def get_all_teams(self):
        """Return all teams."""
        return self.team_repo.teams
    
    def get_team(self, team_name: str) -> Optional[Team]:
        """Return a team by name, or None if not found."""
        return self.team_repo.get_team(team_name)
    
    def does_team_exist(self, team_name: str) -> bool:
        """Check if a team exists."""
        team = self.team_repo.get_team(team_name.lower())
        if team is None:
            return False
        return team.name.lower() == team_name.lower()
        
    def sort_teams_into_a_list_of_tens(self) -> list:
        """Delegate pagination logic to ListOfTeamsLogic."""
        logic = ListOfTeamsLogic()
        return logic.sort_teams_into_a_list_of_tens()