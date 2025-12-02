# LL/tournamentmanager.py

class TournamentManager:
    """Handles creating and storing tournaments in memory."""

    def __init__(self):
        # Holds all tournaments created
        self._tournaments = [] # List of dicts (can be Tournament objects later)

    
