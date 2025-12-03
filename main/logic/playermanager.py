from main.models.playermodel import Player
from main.repo.playerrepo import PlayerRepository

class PlayerManager:
    def __init__(self):
        self.repo = PlayerRepository()

    def register_player(self, name, dob, address, phone, email, url, username, team):
        player_id = self.repo.get_next_id()

        new_player = Player(player_id, name, dob, address, phone, email, url, username, team)
        self.repo.add_player(new_player)
        return new_player    