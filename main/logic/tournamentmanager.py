from datetime import datetime, date
from typing import List, Dict, Optional
import os
import random

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
        "Generates 8 matches for the first round of a 16-team tournament."
        tournament = self.get_tournament(tournament_name)
        if tournament is None:
            raise ValueError("Tournament does not exist.")
        if len(tournament.teams) != 16:
            raise ValueError("Tournament must have exactly 16 teams to generate matches.")

        #Shuffle teams for randomness
        teams = tournament.teams.copy()
        random.shuffle(teams)

        match_ids = []

        #Pair teams into 8 matches
        for i in range(0, 16, 2):
            team1 = teams[i]
            team2 = teams[i + 1]

            match_data = self.match_manager.create_tournament_match(
                team1 = team1, 
                team2 = team2,
                bracket = "WB",
                round_number = 1,
                tournament_id = tournament.tournament_id
                )

            match_ids.append(match_data.match_id)

            #Create the folder automatically inside tournament folder
            tournament_folder = f"tournament_{tournament.name}"
            match_folder = os.path.join(tournament_folder, f"match_{match_data.match_id}")
            os.makedirs(match_folder, exist_ok=True)

            #Create initial 13 placeholder round CSV files
            for round_number in range(1, 14):
                round_path = os.path.join(match_folder, f"round_{round_number}.csv")
                with open(round_path, 'w', encoding='utf-8') as f:
                    f.write("match_id,round,winner,loser,bracket\n")
                    f.write(f"{match_data.match_id},{round_number},TBD,TBD,WB\n")

        #Save match list into tournament
        tournament.matches = match_ids
        self.tournaments.update_tournament(tournament)

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
        # ^^^^ Má ekki :(

    # Helper methods
    def _get_matches(self, tournament_id, bracket=None, round_number=None):
        matches = self.match_manager.repo.get_all()
        filtered = [m for m in matches if str(m.tournament_id) == str(tournament_id)]

        normalized = []
        for m in filtered:
            # Normalize bracket
            br = m.bracket.strip().upper() if m.bracket else ""
            if br == "W":
                br = "WB"
            if br == "L":
                br = "LB"

            # Normalize round
            raw_round = getattr(m, "round", None)
            try:
                rn = int(raw_round)
            except:
                rn = None

            m._norm_bracket = br
            m._norm_round = rn
            normalized.append(m)

        if bracket is not None:
            bracket = bracket.upper()
            normalized = [m for m in normalized if m._norm_bracket == bracket]

        if round_number is not None:
            try:
                round_number = int(round_number)
            except:
                pass
            normalized = [m for m in normalized if m._norm_round == round_number]

        return normalized
    
    def generate_next_rounds(self, tournament_name: str):
        #Generate WB round 2 and LB round 1 for a 16-team double elimination tournament.
        tournament = self.get_tournament(tournament_name)
        if not tournament:
            raise ValueError("Tournament does not exist.")
        
        tid = tournament.tournament_id
        #WB Round 1
        wb_r1_matches = self._get_matches(tid, bracket="WB", round_number="1")
        if len(wb_r1_matches) != 8:
            raise ValueError("WB Round 1 must have exactly 8 matches.")
        
        #Ensure they are all finished
        if any(m.winner is None or m.loser is None for m in wb_r1_matches):
            raise ValueError("Not all WB Round 1 matches are completed.")
        
        #Sort them by match_id to ensure consistent pairing
        wb_r1_matches = sorted(wb_r1_matches, key=lambda m: int(m.match_id))

        #Winners go to WB Round 2
        winners = [m.winner for m in wb_r1_matches]
        #wb_r2_pairs = [(winners[i], winners[i+1]) for i in range(0, len(winners), 2)]
        wb_r2_pairs = [
            (winners[0], winners[1]),
            (winners[2], winners[3]),
            (winners[4], winners[5]),
            (winners[6], winners[7]),
        ]

        #Losers go to LB Round 1
        losers = [m.loser for m in wb_r1_matches]
        lb_r1_pairs = [
            (losers[0], losers[1]),
            (losers[2], losers[3]),
            (losers[4], losers[5]),
            (losers[6], losers[7]),
        ]

        #Check if we already have these matches, avoid duplicates
        existing_wb_r2 = self._get_matches(tid, bracket="WB", round_number=2)
        existing_lb_r1 = self._get_matches(tid, bracket="LB", round_number=1)

        if existing_wb_r2 or existing_lb_r1:
            raise ValueError("Next round matches already exist.")
        
        #Create WB Round 2 matches
        for team1, team2 in wb_r2_pairs:
            self.match_manager.create_tournament_match(
                team1=team1,
                team2=team2,
                bracket="WB",
                round_number=2,
                tournament_id=tournament.tournament_id
            )
        
        #Create LB Round 1 matches
        for team1, team2 in lb_r1_pairs:
            self.match_manager.create_tournament_match(
                team1=team1,
                team2=team2,
                bracket="LB",
                round_number=1,
                tournament_id=tournament.tournament_id
            )

        #Persist to CSV
        self.match_manager.repo.save_to_file()
        print("Next round matches generated successfully.")
        