from typing import List, Optional

from main.IO.IOpy.playerIO import PlayerIO
from main.models.playermodel import Player

class PlayerRepository:
    """Repository responsible for loading, storing and updating Player objects. Players are loaded from CSV on initialization and kept in memory."""
    def __init__(self) -> None:
        self.io = PlayerIO()
        self.players: List[Player] = self.load_players()

    def load_players(self) -> List[Player]:
        """Load players from CSV and convert them into Player objects."""
        rows = self.io.read_file()
        players: List[Player] = []

        for row in rows:
            if row[0] == 'playerID':
                continue  # Skip header row
            
            p = Player(*row)
            players.append(p)

        return players
    
    def save_players(self) -> None:
        """Persist all players back to the CSV file."""
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

    # Internal helpers

    def _get_next_id(self) -> int:
        """Return the next available player ID."""
        if not self.players:
            return 1
        max_id = max(int(player.player_id) for player in self.players)
        return max_id + 1
        
    # Public API

    def add_player(self, player: Player) -> None:
        """Add a new player and persist the change."""
        self.players.append(player)
        self.save_players()

    def get_next_id(self) -> int:
        """Expose next available player ID."""
        return self._get_next_id()
    
    def get_by_name(self, name: str) -> Optional[Player]:
        """Return a player by full name, or None if not found."""
        for p in self.players:
            if p.name == name:
                return p
        return None
    
    def get_by_handle(self, handle: str) -> Optional[Player]:
        """Return a player by username (handle), or None if not found."""
        for p in self.players:
            if p.username == handle:
                return p
        return None
    
    def update_player(self, player):
        """Replace an existing player with updated data and persist changes."""
        for idx, p in enumerate(self.players):
            if p.player_id == player.player_id:
                self.players[idx] = player
                self.save_players()
                return
        raise ValueError("Player not found in repository")