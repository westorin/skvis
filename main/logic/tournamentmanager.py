# LL/tournamentmanager.py

from datetime import datetime # # # # # # # # # # # # # # # Klára að bæta við
from typing import List, Dict # Type hinting
from main.repo.tournamentrepo import TournamentRepository

class TournamentManager:
    """Handles creating and storing tournaments in memory."""

    def __init__(self) -> None:
        # Holds all tournaments created
        self.repo = TournamentRepository()
        
    def create_tournament(self, data: Dict) -> Dict:
        """Creates a new tournament and stores it in the list."""

        name = data["name"]

        # Check if the name is unique
        if self.get_tournament(name) is not None:
            raise ValueError("Tournament name must be unique")
        
        # Create a dict representing the tournament
        tournament: Dict = {
            "name": name,
            "start_date": data["start_date"],
            "end_date": data["end_date"],
            "location": data["location"],
            "contact_email": data["contact_email"],
            "contact_phone": data["contact_phone"],
            "teams": [],      # Will hold teams later
            "matches": [],    # Will hold matches later
            "winner": None,   # Can be a team later
        }
        
        # Store it
        self.repo.add_tournament(tournament)

        # Return it, so caller can use it if needed
        return tournament
    
    def get_tournament(self, name: str) -> Dict | None:
        """Return tournament with this name, or None."""
        return self.repo.get_by_name(name)
    
    def list_tournaments(self) -> List[Dict]:
        """Return list of all tournaments."""
        return self.repo.get_all()