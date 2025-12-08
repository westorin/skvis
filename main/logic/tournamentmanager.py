# LL/tournamentmanager.py

from datetime import datetime, date
from typing import List, Dict, Optional
import os

from main.models.tournamentmodel import Tournament
from main.repo.tournamentrepo import TournamentRepository
from main.repo.teamrepo import TeamRepository
from main.logic.matchmanager import MatchManager
class TournamentManager:
    """Handles creating and storing tournaments in memory + CSV."""

    def __init__(self, tournaments: TournamentRepository, teams: TeamRepository, match_manager: MatchManager) -> None:
        self.tournaments = tournaments
        self.teams = teams
        self.match_manager = match_manager

    # Basic queries

    def get_tournament(self, name: str) -> Optional[Tournament]:
        return self.tournaments.get_by_name(name)
    
    def list_tournaments(self) -> List[Tournament]:
        return self.tournaments.get_all()
    
    # Creation
    
    def create_tournament(self, data: Dict) -> Tournament:
        """Creates a new tournament and stores it in the repo."""

        name = data["name"].strip()

        if self.get_tournament(name) is not None:
            raise ValueError("Tournament name must be unique.")

        start, end = self.validate_dates(data["start"], data["end"])

        tournament_id = self.tournaments.get_next_id()

        tournament = Tournament(
            tournament_id=tournament_id,
            name=name,
            start=start,
            end=end,
            location=data["location"],
            contact_email=data["contact_email"],
            contact_phone=data["contact_phone"],
        )
        
        self.tournaments.add_tournament(tournament)
        return tournament

    # Team registration

    def register_team(self, tournament_name: str, team_name: str) -> Tournament:
        """Add a team to a tournament by name."""

        tournament = self.tournaments.get_by_name(tournament_name)
        if tournament is None:
            raise ValueError("Tournament does not exist.")
        
        team = self.teams.get_team(team_name)
        if team is None:
            raise ValueError("Team does not exist.")
        
        if team_name in tournament.teams:
            raise ValueError("Team is already registered in this tournament.")
        
        tournament.teams.append(team_name)
        self.tournaments.save()
        return tournament

    def is_team_registered(self, tournament_name: str, team_name: str) -> bool:
        tournament = self.tournaments.get_by_name(tournament_name)
        if tournament is None:
            return False
        return team_name in tournament.teams
    
    def set_teams_for_tournament(self, tournament_name: str, team_names: List[str]) -> None:
        tournament = self.get_tournament(tournament_name)
        # Tournament should have exactly 16 teams
        if len(team_names) != 16:
            raise ValueError("Exactly 16 teams are required for the tournament.")
        
        # Verify all teams exist
        for name in team_names:
            if self.teams.get_team(name) is None:
                raise ValueError(f"Team '{name}' does not exist.")
            
        # Remove duplicates while preserving order
        tournament.teams = list(dict.fromkeys(team_names))

        self.tournaments.update_tournament(tournament)

    def generate_initial_matches(self, tournament_name: str) -> None:
        pass
    
    # Date validation

    def validate_dates(self, start: str, end: str) -> tuple[str, str]:
        try:
            start_date = datetime.strptime(start.strip(), "%d-%m-%Y").date()
            end_date = datetime.strptime(end.strip(), "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Invalid date format, use DD-MM-YYYY")

        if end_date < start_date:
            raise ValueError("End date cannot be before start date")

        return start_date.isoformat(), end_date.isoformat()
    
    def analyze_date_string(self, value: str) -> date:
        """Analyzes stored date strings (ISO or DD-MM-YYYY) and changes them into date objects."""
        try:
            return date.fromisoformat(value.strip())
        except ValueError:
            return datetime.strptime(value.strip(), "%d-%m-%Y").date()

    def get_timeframe(self, tournament: Tournament, reference_date: Optional[date] = None) -> str:
        """ - """ # Comment her
        today = reference_date or date.today()
        start_date = self.analyze_date_string(tournament.start)
        end_date = self.analyze_date_string(tournament.end)

        if end_date < today:
            return "Past"
        if start_date > today:
            return "Future"
        return "On going"

    def group_by_timeframe(self, reference_date: Optional[date] = None) -> Dict[str, List[Tournament]]:
        """Group tournaments into Past/On going/Future for the UI layer."""
        group: Dict[str, List[Tournament]] = {"Past": [], "On going": [], "Future": []}
        for tournament in self.list_tournaments():
            timeframe = self.get_timeframe(tournament, reference_date)
            group[timeframe].append(tournament)
        return group
    
    def export_tournament_results(self, tournament_name: str, base_patch: str) -> None:
        "Creates a folder for the tournament, inside it creates 16 match folders"
        "and inside each match folder creates placeholder round files"

        tournament = self.get_tournament(tournament_name)
        if tournament is None:
            raise ValueError("Tournament does not exist.")
        
        #Create main folder
        tournament_folder = os.path.join(base_patch, tournament.name)
        os.makedirs(tournament_folder, exist_ok=True)

        #Create 16 match folders
        for match_index in range(1, 17):
            match_folder = os.path.join(tournament_folder, f"Match_{match_index}")
            os.makedirs(match_folder, exist_ok=True)

            #Create placeholder round files
            for round_number in range(1, 14):  # Assuming 13 rounds per match
                round_file_path = os.path.join(match_folder, f"Round_{round_number}.csv")
                if not os.path.exists(round_file_path):
                    with open(round_file_path, 'w', encoding='utf-8') as f:
                        f.write("match,round,winner,loser,bracket\n")
                        f.write(f"{match_index},{round_number},TBD,TBD,TBD\n")
        print(f"Tournament results exported to {tournament_folder}")
        
        