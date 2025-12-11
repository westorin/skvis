from main.models.playermodel import Player

class PlayerManager:
    def __init__(self,player_repo,team_manager=None):
        self.player_repo = player_repo
        self.team_manager = team_manager

    def register_player(self, name, dob, address, phone, email, url, username, team):
        player_id = self.player_repo.get_next_id()

        new_player = Player(player_id, name, dob, address, phone, email, url, username, team)
        self.player_repo.add_player(new_player)
        return new_player    

    def update_player(self, player_name, name=None, dob=None, address=None, phone=None, email=None, url=None, username=None, team=None):
        player = self.player_repo.get_by_handle(player_name)
        if not player:
            raise ValueError("Player not found")

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
        if username is not None:
            self.team_manager.update_username_in_teams(player_name, username)
        # Sync team assignment only when changed
        if team is not None and team != player.team:
            self.team_manager.update_player_team(player.username, team)

        self.player_repo.update_player(player)
        return player
    
    def does_player_exist(self, player_name):
        team = self.player_repo.get_by_handle(player_name.lower())
        if team is None:
            return False
        if (team.name).lower() == player_name.lower():
            return True
        
    def get_all_players(self):
        """Return all players from the repository."""
        return self.player_repo.players
    
    def get_public_player_rows(self):
        """Public-safe list of players. Doesn't return personal info."""
        rows = []
        for p in self.player_repo.players:
            rows.append([p.username, p.team])
        return rows
    
    def get_private_player_rows_for_user(self, current_user):
        """Role based view of player data. Returns personal info for Admin and Captain."""
        role = getattr(current_user, "role", "player")

        # Admin: see everyone
        if role in "admin":
            rows = []
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
                    p.role,
                ])
            return rows
        
        # Captain: only own team
        if role == "captain":
            captain_team = getattr(current_user, "team", None)

            if (not captain_team) and self.team_manager is not None:
                team = self.team_manager.get_team_by_captain(current_user.username)
                captain_team = team.name if team else None

            if not captain_team:
                return [] # Captain without a team: nothing to show
            
            rows = []
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
                        p.role,
                    ])
            return rows
        
        return self.get_public_player_rows()
    
    def update_player_contact_as_captain(
        self,
        current_user,
        player_handle: str,
        address: str | None = None,
        phone: str | None = None,
        email: str | None = None,
        url: str | None = None,
    ):
        """Allow a captain to update contact info for players on their own team. No team or username changes."""
        role = getattr(current_user, "role", None)
        if role != "captain":
            raise PermissionError("Only captains can use this action.")
        
        # Find captain's team
        captain_team = getattr(current_user, "team", None)
        if (not captain_team) and self.team_manager is not None:
            team = self.team_manager.get_team_by_captain(current_user.username)
            captain_team = team.name if team else None
        
        if not captain_team:
            raise PermissionError("Captain is not assigned to any team.")
        
        # Load player
        player = self.player_repo.get_by_handle(player_handle)
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

        # No team/username changes here on purpose

        self.player_repo.update_player(player)
        return player