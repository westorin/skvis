# LL/tournamentmanager.py

from typing import List, Dict # Type hinting

class TournamentManager:
    """Handles creating and storing tournaments in memory."""

    def __init__(self) -> None:
        # Holds all tournaments created
        self._tournaments: List[Dict] = [] # List of dicts (can be Tournament objects later)

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
        self._tournaments.append(tournament)

        # Return it, so caller can use it if needed
        return tournament
    
    def get_tournament(self, name: str) -> Dict | None:
        """Return the tournament with this name, or None if not found."""
        for t in self._tournaments:
            if t["name"] == name:
                return t
        return None
    
    def list_tournaments(self) -> List[Dict]:
        """Return a list of all tournaments."""
        return list(self._tournaments)