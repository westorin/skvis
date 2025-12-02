# LL/tournamentmanager.py

class TournamentManager:
    """Handles creating and storing tournaments in memory."""

    def __init__(self):
        # Holds all tournaments created
        self._tournaments = list[dict] = [] # List of dicts (can be Tournament objects later)

    def create_tournament(self, data: dict) -> dict:
        """Creates a new tournament and stores it in the list."""

        name = data["name"]

        # Check if the name is unique
        if self.get_tournament(name) is not None:
            raise ValueError("Tournament name must be unique")
        
        # Create a dict representing the tournament
        tournament: dict = {
            "name": name,
            "start_date": data["start_date"],
            "end_date": data["end_date"],
            "location": data["location"],
            "contact_email": data["contact_email"],
            "contact_phone": data["contact_phone"],
            "teams": [], # Will hold teams later
            "matches": [], # Will hold matches later
            "winner": [], # Later can be a team
        }

        # Store it
        self._tournaments.append(tournament)

        # Return it, so caller can use it if needed
        return tournament