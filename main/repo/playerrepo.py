from main.IO.IOpy.playerIO import PlayerIO
from main.models.playermodel import Player

class PlayerRepository:
    def __init__(self):
        self.io = PlayerIO()
        self.players = self.load_players()

    # Load players from storage
    def load_players(self):
        rows = self.io.read_file()
        players = []
        for row in rows:
            if row[0] == 'playerID':
                continue  # Skip header row
            else:
                p = Player(*row)
                players.append(p)

        return players
    
    # Internal helper to get next ID
    def _get_next_id(self):
        if not self.players:
            return 1
        else:
            max_id = max(int(player.player_id) for player in self.players)
            return max_id + 1
        
    # Add a new player
    def add_player(self, player):
        self.players.append(player)
        self.save_players()

    # Save players to storage
    def save_players(self):
        rows = [["playerID","name","dob","address","phone","email","url","username","team"]]
        for p in self.players:
            rows.append([
                p.player_id,
                p.name,
                p.dob,
                p.address,
                p.phone,
                p.email,
                p.url,
                p.username,
                p.team
            ])
        self.io.write_file(rows)

    # Get the next available player ID
    def get_next_id(self):
        return self._get_next_id()
    
    # Get player by name
    def get_by_name(self, name:str):
        for p in self.players:
            if p.name == name:
                return p
        return None
    
    # Get player by handle (username)
    def get_by_handle(self, handle:str):
        for p in self.players:
            if p.username == handle:
                return p
        return None
    
    # Update existing player
    def update_player(self, player):
        for idx, p in enumerate(self.players):
            if p.player_id == player.player_id:
                self.players[idx] = player
                self.save_players()
                return
        raise ValueError("Player not found in repository")