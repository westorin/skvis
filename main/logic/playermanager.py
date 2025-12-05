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