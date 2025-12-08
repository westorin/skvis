# main/models/tournamentmodel.py

from typing import List, Optional # Má nota optional?

class Tournament:
    def __init__(self, name: str, start: str, end: str, location: str, contact_email: str, contact_phone: str, teams: Optional[List[str]] = None, matches: Optional[list] = None, winner: Optional[str] = None, tournament_id: Optional[int] = None,) -> None:
        self.tournament_id = tournament_id
        self.name = name
        self.start = start
        self.end = end
        self.location = location
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.teams: List[str] = teams or [] # list of team names
        self.matches = matches or [] # fill later when scheduling
        self.winner = winner

        # Bæta við (type hinting) í __init__
       