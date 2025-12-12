from main.models.playermodel import Player
from typing import Optional, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from main.repo.playerrepo import PlayerRepository
    from main.logic.teammanager import TeamManager

class PlayerManager:
    """Logic for creating, updating and viewing players."""
    def __init__(self, player_repo: "PlayerRepository", team_manager: Optional["TeamManager"] = None) -> None:
        """Arguements: player_repo: Repository for storing/retrieving players.
                       team_manager: Optional manager used to sync team/username changes."""
        self.player_repo = player_repo
        self.team_manager = team_manager

    def register_player(self, name: str, dob: str, address: str, phone: str, email: str, url: str, username: str, team: str) -> Player:
        """Register a new player and store them in the repository. Returns the created player."""
        player_id: int = self.player_repo.get_next_id()
        new_player: Player = Player(player_id, name, dob, address, phone, email, url, username, team)
        self.player_repo.add_player(new_player)
        return new_player    

    def update_player(self, player_name: str, name: Optional[str] = None, dob: Optional[str] = None, address: Optional[str] = None, phone: Optional[str] = None, email: Optional[str] = None, url: Optional[str] = None, username: Optional[str] = None, team: Optional[str] = None) -> Player:
        """Update an existing player by their handle/username."""
        player: Optional[Player] = self.player_repo.get_by_handle(player_name)
        if not player:
            raise ValueError("Player not found")

        # Save old values so we can correctly detect changes after updates
        old_username: str = player.username
        old_team: str = player.team

        # Apply updates
        if name is not None:
            player.name = name
        if dob is not None:
            player.dob = dob
        if address is not None:
            player.address = address
        if phone is not None:
            player.phone = phone
        if email is not None:
            player.email = email
        if url is not None:
            player.url = url
        if username is not None:
            player.username = username
        if team is not None:
            player.team = team

        # Sync username changes in all teams
        if username is not None and self.team_manager is not None:
            self.team_manager.update_username_in_teams(old_username, username)

        # Sync team assignment only when changed
        if team is not None and team != old_team and self.team_manager is not None:
            self.team_manager.update_player_team(player.username, team)

        self.player_repo.update_player(player)
        return player
    
    def does_player_exist(self, player_name: str) -> bool:
        """Check if a player exists by handle/name."""
        player = self.player_repo.get_by_handle(player_name.lower())
        if player is None:
            return False
        return player.name.lower() == player_name.lower()
        
    def get_all_players(self) -> list[Player]:
        """Return all players from the repository."""
        return self.player_repo.players
    
    def get_public_player_rows(self) -> list[list[str]]:
        """Public-safe list of players. Doesn't return personal info."""
        rows: list[list[str]] = []
        for p in self.player_repo.players:
            rows.append([p.username, p.team])
        return rows
    
    def get_private_player_rows_for_user(self, current_user: Any) -> list[list[Any]]:
        """Role based view of player data. Returns personal info for Admin and Captain."""
        role: str = getattr(current_user, "role", "player")

        # Admin: see everyone
        if role == "admin":
            rows: list[list[Any]] = []
            for p in self.player_repo.players:
                rows.append([
                    p.username,
                    p.name,
                    p.dob,
                    p.address,
                    p.phone,
                    p.email,
                    p.url,
                    p.team,
                    getattr(p, "role", "player"),
                ])
            return rows
        
        # Captain: only own team
        if role == "captain":
            captain_team: Optional[str] = getattr(current_user, "team", None)

            # If current_user.team is missing, try to resolve via TeamManager
            if (not captain_team) and self.team_manager is not None:
                team = self.team_manager.get_team_by_captain(current_user.username)
                captain_team = team.name if team else None

            if not captain_team:
                return [] # Captain without a team: nothing to show
            
            rows: list[list[Any]] = []
            for p in self.player_repo.players:
                if p.team == captain_team:
                    rows.append([
                        p.username,
                        p.name,
                        p.dob,
                        p.address,
                        p.phone,
                        p.email,
                        p.url,
                        p.team,
                        getattr(p, "role", "player"),
                    ])
            return rows
        
        return self.get_public_player_rows()
    
    def update_player_contact_as_captain(
        self,
        current_user: Any,
        player_handle: str,
        address: Optional[str] = None,
        phone: Optional[str] = None,
        email: Optional[str] = None,
        url: Optional[str] = None,
    ) -> Player:
        """Allow a captain to update contact info for players on their own team. No team or username changes."""
        role = getattr(current_user, "role", None)
        if role != "captain":
            raise PermissionError("Only captains can use this action.")
        
        # Find captain's team
        captain_team: Optional[str] = getattr(current_user, "team", None)
        if (not captain_team) and self.team_manager is not None:
            team = self.team_manager.get_team_by_captain(current_user.username)
            captain_team = team.name if team else None
        
        if not captain_team:
            raise PermissionError("Captain is not assigned to any team.")
        
        # Load player
        player: Optional[Player] = self.player_repo.get_by_handle(player_handle)
        if not player:
            raise ValueError("Player not found.")
        
        # Ensure player belongs to captain's team
        if player.team != captain_team:
            raise PermissionError("Captains can only edit players in their own team.")
        
        # Apply contact changes
        if address is not None:
            player.address = address
        if phone is not None:
            player.phone = phone
        if email is not None:
            player.email = email
        if url is not None:
            player.url = url

        self.player_repo.update_player(player)
        return player