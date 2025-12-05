# LL/tournamentmanager.py

from datetime import datetime
from typing import List, Dict
from main.models.tournamentmodel import Tournament

class TournamentManager:
    """Handles creating and storing tournaments in memory + CSV."""

    def __init__(self, tournaments, teams) -> None:
        self.tournaments = tournaments
        self.teams = teams

    def get_tournament(self, name: str) -> Tournament | None:
        return self.tournaments.get_by_name(name)
    
    def create_tournament(self, data: Dict) -> Tournament:
        """Creates a new tournament and stores it in the list."""

        name = data["name"].strip()

        # Check name ASAP to fail fast on bad input
        if self.get_tournament(name) is not None:
            raise ValueError("Tournament name must be unique.")

        start, end = self.validate_dates(data["start"], data["end"])

        tournament = Tournament(
            name=name,
            start=start,
            end=end,
            location=data["location"],
            contact_email=data["contact_email"],
            contact_phone=data["contact_phone"],
        )
        
        self.tournaments.add_tournament(tournament)

        return tournament

    # def register_team(tournament, team):
        
    # def generate_schedule(tournament):

    def validate_dates(self, start: str, end: str) -> tuple[str, str]:
        try:
            start_date = datetime.strptime(start.strip(), "%d-%m-%Y").date()
            end_date = datetime.strptime(end.strip(), "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format, use DD-MM-YYYY")

        if end_date < start_date:
            raise ValueError("End date cannot be before start date")

        return start_date.isoformat(), end_date.isoformat()

    # def is_team_registered(tournament, team):

    def list_tournaments(self) -> List[Tournament]:
        return self.tournaments.get_all()
    
    # def get_schedule(tournament):
