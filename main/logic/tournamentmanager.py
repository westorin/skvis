# LL/tournamentmanager.py

from datetime import datetime
from typing import List, Dict
from main.repo.tournamentrepo import TournamentRepository
from main.models.tournamentmodel import Tournament

class TournamentManager:
    """Handles creating and storing tournaments in memory + CSV."""

    def __init__(self) -> None:
        self.repo = TournamentRepository()

    def get_tournament(self, name: str) -> Tournament | None:
        return self.repo.get_by_name(name)
    
    def create_tournament(self, data: Dict) -> Tournament:
        """Creates a new tournament and stores it in the list."""

        name = data["name"]

        # Check if the name is unique
        if self.get_tournament(name) is not None:
            raise ValueError("Tournament name must be unique.")
        
        tournament = Tournament(
            name=name,
            start=data["start"],
            end=data["end"],
            location=data["location"],
            contact_email=data["contact_email"],
            contact_phone=data["contact_phone"],
        )
        
        self.repo.add_tournament(tournament)

        return tournament

    # def register_team(tournament, team):
        
    # def generate_schedule(tournament):

    def validate_dates(self, start: str, end: str) -> None:
        try:
            start = datetime.strptime(start, "%d-%m-%Y").date()
            end = datetime.strptime(end, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format, use DD-MM-YYYY")

        if end < start:
            raise ValueError("End date cannot be before start date")

    # def is_team_registered(tournament, team):

    def list_tournaments(self) -> List[Tournament]:
        return self.repo.get_all()
    
    # def get_schedule(tournament):