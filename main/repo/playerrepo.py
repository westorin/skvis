from main.IO.playerIO import PlayerIO
from main.models.playermodel import Player

class PlayerRepository:
    def __init__(self):
        self.io = PlayerIO()
        self.players = self.load_players()

    def load_players(self):
        rows = self.io.read_file()
        players = []
        for row in rows:
            if row[0] == 'playerID':
                p = Player(*row)
                players.append(p)
        return players
    
    def _get_next_id(self):
        if not self.players:
            return 1
        else:
            max_id = max(int(player.player_id) for player in self.players)
            return max_id + 1
        
    def add_player(self, player):
        self.players.append(player)
        self.save_players()

    def save_players(self):
        rows = ["playerId,name,dob,address,phone,email,url,username,team"]
        for p in self.players:
            rows.append(f"{p.player_id},{p.name},{p.dob},{p.address},{p.phone},{p.email},{p.url},{p.username},{p.team}")
        self.io.write_file(rows)

    def get_next_id(self):
        return self._get_next_id()