from main.models.playermodel import Player
from main.repo.playerrepo import PlayerRepository

class PlayerManager:
    def __init__(self):
        self.player_repo = PlayerRepository()

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

        self.player_repo.update_player(player)
        return player