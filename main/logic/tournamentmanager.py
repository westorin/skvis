from datetime import datetime, date, timedelta
from typing import List, Dict, Tuple, Optional, Any, TYPE_CHECKING
import os
import csv
import random

from main.models.tournamentmodel import Tournament
from main.repo.tournamentrepo import TournamentRepository
from main.repo.teamrepo import TeamRepository
from main.logic.matchmanager import MatchManager

if TYPE_CHECKING:
    from main.models.matchmodel import Match

class TournamentManager:
    """Handles creating tournaments, registering teams, generating matches, scheduling matches and exporting results to CSV."""
    def __init__(self, tournaments: TournamentRepository, teams: TeamRepository, match_manager: MatchManager) -> None:
        self.tournaments = tournaments
        self.teams = teams
        self.match_manager = match_manager

    # Basic queries

    def get_tournament(self, name: str) -> Optional[Tournament]:
        """Return a tournament by name, or None if not found."""
        return self.tournaments.get_by_name(name)
    
    def list_tournaments(self) -> List[Tournament]:
        """Return all tournaments."""
        return self.tournaments.get_all()
    
    # Creation
    
    def create_tournament(self, data: Dict[str, Any]) -> Tournament:
        """Creates a new tournament and stores it in the repository."""
        name: str = str(data["name"]).strip()

        if self.get_tournament(name) is not None:
            raise ValueError("Tournament name must be unique.")

        start, end = self.validate_dates(data["start"], data["end"])

        tournament_id: int = self.tournaments.get_next_id()

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
        """Register a team into a tournament by name."""
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
        """Return True if team_name is registered in tournament_name."""
        tournament = self.tournaments.get_by_name(tournament_name)
        if tournament is None:
            return False
        return team_name in tournament.teams
    
    def set_teams_for_tournament(self, tournament_name: str, team_names: List[str]) -> None:
        """Set the team list for a tournament."""
        tournament = self.get_tournament(tournament_name)
        if tournament is None:
            raise ValueError("Tournament does not exist.")

        # Exactly 16 teams are required
        if len(team_names) != 16:
            raise ValueError("Exactly 16 teams are required for the tournament.")

        # Remove duplicates while preserving order
        unique_names = list(dict.fromkeys(team_names))
        if len(unique_names) != 16:
            raise ValueError("Team names must be unique.")

        # Verify all teams exist and have 3-5 players
        checked_names: List[str] = []
        for name in unique_names:
            team = self.teams.get_team(name)
            if team is None:
                raise ValueError(f"Team '{name}' does not exist.")

            player_count = len(team.players)
            if player_count < 3 or player_count > 5:
                raise ValueError(
                    f"Team '{name}' must have between 3 and 5 players."
                    f"(currently {player_count})."
                )        
            checked_names.append(name)
        
        tournament.teams = checked_names
        self.tournaments.update_tournament(tournament)

    def generate_initial_matches(self, tournament_name: str) -> None:
        "Generates 8 matches for the first round of a 16-team tournament."
        tournament = self.get_tournament(tournament_name)
        if tournament is None:
            raise ValueError("Tournament does not exist.")
        if len(tournament.teams) != 16:
            raise ValueError("Tournament must have exactly 16 teams to generate matches.")

        # Shuffle teams for randomness
        teams = tournament.teams.copy()
        random.shuffle(teams)

        match_ids: List[int] = []

        # Pair teams into 8 matches
        for i in range(0, 16, 2):
            team1 = teams[i]
            team2 = teams[i + 1]

            match_data = self.match_manager.create_tournament_match(
                team1 = team1, 
                team2 = team2,
                bracket = "WB",
                round_number = 1,
                tournament_id = tournament.tournament_id,
                tournament_name = tournament.name,
                )

            match_ids.append(match_data.match_id)

        #Save match list into tournament
        tournament.matches = match_ids
        self.tournaments.update_tournament(tournament)

    # Date validation / timeframe

    def validate_dates(self, start: str, end: str) -> Tuple[str, str]:
        """Validate DD-MM-YYYY input and return ISO strings (YYYY-MM-DD)."""
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
        """Return Past / Ongoing / Future for a given tournament."""
        today = reference_date or date.today()
        start_date = self.analyze_date_string(tournament.start)
        end_date = self.analyze_date_string(tournament.end)

        if end_date < today:
            return "Past"
        if start_date > today:
            return "Future"
        return "Ongoing"

    def group_by_timeframe(self, reference_date: Optional[date] = None) -> Dict[str, List[Tournament]]:
        """Group tournaments into Past/Ongoing/Future for the UI layer."""
        group: Dict[str, List[Tournament]] = {"Past": [], "Ongoing": [], "Future": []}
        for tournament in self.list_tournaments():
            timeframe = self.get_timeframe(tournament, reference_date)
            group[timeframe].append(tournament)
        return group

    def list_past_tournaments(self, reference_date: Optional[date] = None) -> list[Tournament]:
        return self.group_by_timeframe(reference_date)["Past"]

    def list_ongoing_tournaments(self, reference_date: Optional[date] = None) -> list[Tournament]:
        return self.group_by_timeframe(reference_date)["Ongoing"]

    def list_future_tournaments(self, reference_date: Optional[date] = None) -> list[Tournament]:
        return self.group_by_timeframe(reference_date)["Future"]

    # UI helper lists + pagination

    def list_tournaments_basic_info(self) -> List[List[str]]:
        """Return [name, start, end] for all tournaments as simple lists."""
        rows: List[List[str]] = []
        for t in self.list_tournaments():
            rows.append([t.name, t.start, t.end])
        return rows

    def list_tournaments_basic_info_by_timeframe(self, timeframe: str, reference_date: Optional[date] = None) -> List[List[str]]:
        """Return (name, start, end) for tournaments in a specific timeframe. Timeframe must be: 'Past', 'Ongoing', or 'Future'."""
        grouped = self.group_by_timeframe(reference_date)

        if timeframe not in grouped:
            raise ValueError("Invalid timeframe. Use 'Past', 'Ongoing' or 'Future'.")

        rows: List[List[str]] = []
        for t in grouped[timeframe]:
            rows.append([t.name, t.start, t.end])
        return rows

    def sort_into_rows_of_tens(self, rows: List[List[str]], columns: int) -> List[List[List[str]]]:
        """Split rows into pages of 10 rows each. Pads the last page with placeholder rows"""
        remaining_rows = list(rows)
        pages: List[List[List[str]]] = []

        if len(remaining_rows) % 10 == 0:
            page_count = len(remaining_rows) // 10
        else:
            page_count = (len(remaining_rows) // 10) + 1
        
        for _ in range(page_count):
            current_page: List[List[str]] = []

            if (len(remaining_rows) // 10) > 0:
                # Full page
                for _ in range(10):
                    current_page.append(remaining_rows[0])
                    remaining_rows = remaining_rows[1:]
                pages.append(current_page)
            
            elif (len(remaining_rows) // 10) == 0 and len(remaining_rows) % 10 != 0:
                # Partial page
                for row in remaining_rows:
                    current_page.append(row)
                remaining_rows = []

                # Pad with empty rows
                missing = 10 - len(current_page)
                for _ in range(missing):
                    current_page.append([""] * columns)
                
                pages.append(current_page)
        
        return pages
    
    # Scheduling + schedule/result views

    def schedule_matches(self, tournament_name: str, start_date: str, start_time: str, servers: int, slot_minutes: int = 60) -> List[List[Any]]:
        """Assign date, time and server_id to all matches in a tournament"""
        if servers <= 0:
            raise ValueError("Servers must be at least 1.")
        
        tournament = self.get_tournament(tournament_name)
        if tournament is None:
            raise ValueError("Tournament does not exist.")
        
        try:
            base_date = datetime.strptime(start_date.strip(), "%d-%m-%Y").date()
            base_time = datetime.strptime(start_time.strip(), "%H:%M").time()
        except ValueError:
            raise ValueError("Invalid date or time format. Use DD-MM-YYYY and HH:MM.")
        
        base_dt = datetime.combine(base_date, base_time)

        # Get all matches for this tournament
        matches: List[Any] = [
            m for m in self.match_manager.repo.get_all()
            if str(m.tournament_id) == str(tournament.tournament_id)
        ]

        if not matches:
            raise ValueError("No matches found for this tournament.")
        
        # Sort by [round, bracket, match_id] for a stable, bracket-respecting order
        def sort_key(m: Any) -> List[Any]:
            try:
                rnd = int(m.round) if m.round is not None else 0
            except (ValueError, TypeError):
                rnd = 0
            br = (m.bracket or "").upper()
            try:
                mid = int(m.match_id)
            except:
                mid = 0
            return [rnd, br, mid]
        
        matches = sorted(matches, key=sort_key)

        # slot_index -> list of [match, server_index]
        slots: Dict[int, List[List[Any]]] = {}

        for match in matches:
            slot_index = 0
            while True:
                slot_matches = slots.get(slot_index, [])

                # Check the server capacity
                if len(slot_matches) < servers:

                    # Check team conflict
                    conflict = False
                    for existing_match, _ in slot_matches:
                        if (
                            existing_match.team1 in (match.team1, match.team2)
                            or existing_match.team2 in (match.team1, match.team2)
                        ):
                            conflict = True
                            break
                    
                    if not conflict:
                        server_index = len(slot_matches) + 1
                        slot_matches.append([match, server_index])
                        slots[slot_index] = slot_matches
                        break
                
                slot_index += 1
        
        # Assign date/time/server_id
        result_rows: List[List[Any]] = []

        for slot_index in sorted(slots.keys()):
            match_dt = base_dt + timedelta(minutes=slot_index * slot_minutes)
            date_str = match_dt.date().isoformat()
            time_str = match_dt.strftime("%H:%M")

            for pair in slots[slot_index]:
                match = pair[0]
                server_index = pair[1]

                match.date = date_str
                match.time = time_str
                match.server_id = f"SRV-{server_index}"

                result_rows.append([
                    match.match_id,
                    match.team1,
                    match.team2,
                    match.date,
                    match.time,
                    match.server_id
                ])
        
        # Persist changes
        self.match_manager.repo.save_to_file()
        return result_rows
        
    def get_schedule_basic(self, tournament_name: str) -> List[List[str]]:
        """Returns a schedule for one tournament, each row is: [game_nr, team_a, team_b, date, start_time, location]"""
        tournament = self.get_tournament(tournament_name)
        if tournament is None:
            raise ValueError("Tournament does not exist.")
        
        tid = tournament.tournament_id
        matches = self._get_matches(tid)
        matches = sorted(matches, key=lambda m: int(m.match_id))

        rows: List[List[str]] = []
        for idx, m in enumerate(matches, start=1):
            date_val = getattr(m, "date", "") or ""
            if not date_val:
                date_val = getattr(tournament, "start", "") or ""
        
            time_val = getattr(m, "time", "") or ""
            if not time_val:
                time_val = "18:00" # Default time for all matches
        
            location_val = getattr(m, "location", None)
            if not location_val:
                location_val = getattr(tournament, "location", "") or ""

            rows.append([
                str(idx),
                m.team1 or "",
                m.team2 or "",
                date_val,
                time_val,
                location_val,
            ])
    
        return rows 
    
    def get_schedule_pages(self, tournament_name: str) -> List[List[List[str]]]:
        """Return schedule rows goruped into pages of 10."""
        rows = self.get_schedule_basic(tournament_name)
        return self.sort_into_rows_of_tens(rows, columns=6)

    def get_results_basic(self, tournament_name: str) -> List[List[str]]:
        """Return a list of match results for one tournament. Each row is [match_id, round, bracket, team1, team2, winner, loser, final_score, total_rounds]."""
        tournament = self.get_tournament(tournament_name)
        if tournament is None:
            raise ValueError("Tournament does not exist.")
        
        matches: List[Any] = [
            m for m in self.match_manager.repo.get_all()
            if str(m.tournament_id) == str(tournament.tournament_id)
        ]

        rows: List[List[str]] = []
        for m in matches:
            rows.append([
                str(m.match_id),
                "" if m.round is None else str(m.round),
                "" if m.bracket is None else str(m.bracket),
                m.team1,
                m.team2,
                m.winner or "",
                m.loser or "",
                m.final_score or "",
                str(m.total_rounds or 0),
            ])
        return rows
    
    def get_results_pages(self, tournament_name: str) -> List[List[List[str]]]:
        """Return result rows grouped into pages of 10."""
        rows = self.get_results_basic(tournament_name)
        return self.sort_into_rows_of_tens(rows, columns=9)
    
    # Team -> Tournaments

    def list_tournaments_for_team(self, team_name: str) -> List[Tournament]:
        """Return all tournaments where this team is registered."""
        team_name = team_name.strip()
        result: List[Tournament] = []
        for t in self.tournaments.get_all():
            if team_name in getattr(t, "teams", []):
                result.append(t)
        return result
    
    def list_tournament_names_for_team(self, team_name: str):
        """Convenience: just the tournament names for a given team."""
        return [t.name for t in self.list_tournaments_for_team(team_name)]

    # Internal match helpers

    def _get_matches(self, tournament_id: Any, bracket: Optional[str] = None, round_number: Optional[int] = None) -> List[Any]:
        """Return matches for a tournament, with optional bracket/round filtering."""
        matches = self.match_manager.repo.get_all()
        filtered = [m for m in matches if str(m.tournament_id) == str(tournament_id)]

        normalized: List[Any] = []
        for m in filtered:
            raw_bracket = getattr(m, "bracket", None)
            if raw_bracket is None:
                m._norm_bracket = None
            else:
                b = str(raw_bracket).upper().strip()
                if b == "W":
                    b = "WB"
                elif b == "L":
                    b = "LB"
                m._norm_bracket = b

            raw_round = getattr(m, "round", None)
            try:
                m._norm_round = int(raw_round)
            except (ValueError, TypeError):
                m._norm_round = None

            normalized.append(m)

        if bracket is not None:
            bracket = bracket.upper()
            normalized = [m for m in normalized if m._norm_bracket == bracket]

        if round_number is not None:
            round_number = int(round_number)
            normalized = [m for m in normalized if m._norm_round == round_number]

        return normalized
    
    def generate_next_rounds(self, tournament_name: str) -> None:
        """Generate WB round 2 and LB round 1 for a 16-team double elimination tournament."""
        tournament = self.get_tournament(tournament_name)
        if not tournament:
            raise ValueError("Tournament does not exist.")
        
        tid = tournament.tournament_id
        # WB Round 1
        wb_r1_matches = self._get_matches(tid, bracket="WB", round_number=1)
        if len(wb_r1_matches) != 8:
            raise ValueError("WB Round 1 must have exactly 8 matches.")
        
        # Ensure they are all finished
        if any(m.winner is None or m.loser is None for m in wb_r1_matches):
            raise ValueError("Not all WB Round 1 matches are completed.")
        
        # Sort them by match_id to ensure consistent pairing
        wb_r1_matches = sorted(wb_r1_matches, key=lambda m: int(m.match_id))

        # Winners go to WB Round 2
        winners = [m.winner for m in wb_r1_matches]
        # wb_r2_pairs = [(winners[i], winners[i+1]) for i in range(0, len(winners), 2)]
        wb_r2_pairs = [
            (winners[0], winners[1]),
            (winners[2], winners[3]),
            (winners[4], winners[5]),
            (winners[6], winners[7]),
        ]

        # Losers go to LB Round 1
        losers = [m.loser for m in wb_r1_matches]
        lb_r1_pairs = [
            (losers[0], losers[1]),
            (losers[2], losers[3]),
            (losers[4], losers[5]),
            (losers[6], losers[7]),
        ]

        # Check if we already have these matches, avoid duplicates
        existing_wb_r2 = self._get_matches(tid, bracket="WB", round_number=2)
        existing_lb_r1 = self._get_matches(tid, bracket="LB", round_number=1)

        if existing_wb_r2 or existing_lb_r1:
            raise ValueError("Next round matches already exist.")
        
        # Create WB Round 2 matches
        for team1, team2 in wb_r2_pairs:
            self.match_manager.create_tournament_match(
                team1=team1,
                team2=team2,
                bracket="WB",
                round_number=2,
                tournament_id=tournament.tournament_id,
                tournament_name = tournament.name,
            )
        
        # Create LB Round 1 matches
        for team1, team2 in lb_r1_pairs:
            self.match_manager.create_tournament_match(
                team1=team1,
                team2=team2,
                bracket="LB",
                round_number=1,
                tournament_id=tournament.tournament_id,
                tournament_name = tournament.name,
            )

        #Persist to CSV
        self.match_manager.repo.save_to_file()
        
    def _simulate_round(self, tid, bracket, round_number):
        """Simulate all unfinished matches in a given bracket+round."""
        matches = self._get_matches(tid, bracket=bracket, round_number=round_number)
        for match in matches:
            if match.winner is None:
                self.match_manager.play_match_random(match.match_id)
        self.match_manager.repo.save_to_file()

    def generate_wb_round_3(self, tid: Any) -> None:
        tournament = self.tournaments.get_by_id(tid)
        wb_r2 = self._get_matches(tid, "WB", 2)
        if len(wb_r2) != 4:
            raise ValueError("Not enough WB R2 matches to generate WB R3 semifinals.")
        
        if any(m.winner is None for m in wb_r2):
            raise ValueError("Not all WB R2 matches are completed.")
        
        wb_r2 = sorted(wb_r2, key=lambda m: int(m.match_id))
        winners = [m.winner for m in wb_r2]

        pairs = [
            (winners[0], winners[1]),
            (winners[2], winners[3]),
        ]

        for team1, team2 in pairs:
            self.match_manager.create_tournament_match(
                team1=team1,
                team2=team2,
                bracket="WB",
                round_number=3,
                tournament_id=tid,
                tournament_name = tournament.name,
            )
        self.match_manager.repo.save_to_file()

    def generate_wb_final(self, tid, tournament):
        """Generate WB Final (round 4) from WB Round 3 winners."""
        wb_r3 = self._get_matches(tid, "WB", 3)
        if len(wb_r3) != 2:
            raise ValueError("Not enough WB R3 matches to generate WB Final.")
        
        if any(m.winner is None for m in wb_r3):
            raise ValueError("Not all WB R3 matches are completed.")
        
        wb_r3 = sorted(wb_r3, key=lambda m: int(m.match_id))
        winners = [m.winner for m in wb_r3]

        final_match = self.match_manager.create_tournament_match(
            team1=winners[0],
            team2=winners[1],
            bracket="WB",
            round_number=4,
            tournament_id=tid,
            tournament_name = tournament.name,
        )
        self.match_manager.repo.save_to_file()
        return final_match
    
    def run_full_simulation(self, tournament: Tournament) -> Any:
        """Run a full simulation (WB only in this implementation), export CSVs, return summary dict."""
        tid = tournament.tournament_id
        tname = tournament.name

        # 0 Ensure WB round 1 matches exist
        wb_r1 = self._get_matches(tid, "WB", 1)
        if not wb_r1:
            self.generate_initial_matches(tname)
            wb_r1 = self._get_matches(tid, "WB", 1)

        # 1 Simulate WB Round 1
        self._simulate_round(tid, "WB", 1)

        # 2 Generate WB round 2 matches and LB round 1 matches
        existing_wb_r2 = self._get_matches(tid, "WB", 2)
        if not existing_wb_r2:
            self.generate_next_rounds(tname)
        else:
            return "WB Round 2 and LB Round 1 matches already exist."

        # 3 Simulate WB round 2 matches and LB round 1 matches
        self._simulate_round(tid, "WB", 2)
        self._simulate_round(tid, "LB", 1)

        # 4 Generate WB round 3 matches
        existing_wb_r3 = self._get_matches(tid, "WB", 3)
        if not existing_wb_r3:
            self.generate_wb_round_3(tid)
        else:
            return "WB Round 3 matches already exist."

        # 5 Simulate WB round 3 matches
        self._simulate_round(tid, "WB", 3)

        # 6 Generate WB final match
        existing_wb_final = self._get_matches(tid, "WB", 4)
        if not existing_wb_final:
            final_match = self.generate_wb_final(tid,tournament)
        else:
            final_match = existing_wb_final[0]

        # 7 Simulate WB final match
        self._simulate_round(tid, "WB", 4)

        final_matches = self._get_matches(tid, "WB", 4)
        fm = final_matches[0]
        fm = self.match_manager.repo.get_by_match_id(fm.match_id)

        summary: Dict[str, Any] = {
            "champion": fm.winner,
            "runner_up": fm.loser,
            "final_score": fm.final_score,
            "total_rounds": fm.total_rounds,
        }

        self.export_full_results(tournament, summary)
        return summary
    
    # Export results

    def export_full_results(self, tournament: Tournament, summary: Dict[str, Any]) -> None:
        """
        Export full tournament results for a single tournament in to one CSV file


        The CSV will contain:
        - Summary (tournament, champion, runner-up, final score, total rounds)
        - Final standing
        - Team performance
        - Match summary (per match)        
        """
        tid = tournament.tournament_id
        tname = tournament.name

        # Ensure base directory
        base_dir = os.path.join("main", "IO", tname)
        os.makedirs(base_dir, exist_ok=True)


        # Load matches
        matches = self._get_matches(tid)

        # Build team stats
        team_stats: Dict[str, Dict[str, int]] = {}

        def ensure_team(team_name: str) -> None:
            if team_name not in team_stats:
                team_stats[team_name] = {
                    "matches_played": 0,
                    "wins": 0,
                    "losses": 0,
                    "rounds_won": 0,
                    "rounds_lost": 0,
                }

        for m in matches:
            team1, team2 = m.team1, m.team2
            ensure_team(team1)
            ensure_team(team2)

            team_stats[team1]["matches_played"] += 1
            team_stats[team2]["matches_played"] += 1

            if m.winner and m.loser:
                ensure_team(m.winner)
                ensure_team(m.loser)
                team_stats[m.winner]["wins"] += 1
                team_stats[m.loser]["losses"] += 1

            # Rounds from final_score
            if m.final_score:
                try:
                    t1_score, t2_score = str(m.final_score).split("-")
                    t1,t2 = int(t1_score), int(t2_score)
                    team_stats[team1]["rounds_won"] += t1
                    team_stats[team1]["rounds_lost"] += t2
                    team_stats[team2]["rounds_won"] += t2
                    team_stats[team2]["rounds_lost"] += t1
                except:
                    pass
        
        # Determine standings 1-N
        champion = summary.get("champion")
        runner_up = summary.get("runner_up")

        all_teams = list(team_stats.keys())

        # Compute round diff for sorting
        def round_diff(team: str) -> int:
            stats = team_stats[team]
            return stats["rounds_won"] - stats["rounds_lost"]
        
        # Remove champion and runner-up from the pool if present
        others = [t for t in all_teams if t not in (champion, runner_up)]

        # Sort the rest by wins, round_diff, losses, name
        others_sorted = sorted(
            others,
            key=lambda t: (
                -team_stats[t]["wins"],
                -round_diff(t),
                team_stats[t]["losses"],
                t.lower()
            )
        )

        standings: List[str] = []
        if champion:
            standings.append(champion)
        if runner_up and runner_up != champion:
            standings.append(runner_up)
        standings.extend(others_sorted)

        # Write summary CSV
        summary_path = os.path.join(base_dir, "summary.csv")
        with open(summary_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["field","value"])
            writer.writerow(["tournament", tname])
            writer.writerow(["champion", summary.get("champion")])
            writer.writerow(["runner_up", summary.get("runner_up")])
            writer.writerow(["final_score", summary.get("final_score")])
            writer.writerow(["total_rounds", summary.get("total_rounds")])

        # Write standings
        standings_path = os.path.join(base_dir, "standings.csv")
        with open(standings_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["rank","team"])
            for idx, team in enumerate(standings, start=1):
                writer.writerow([idx, team])

        # Write team performance
        performance_path = os.path.join(base_dir, "performance.csv")
        with open(performance_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["team","matches_played","wins","losses","rounds_won","rounds_lost","round_diff"])

            for team in standings:
                stats = team_stats[team]
                rd = stats["rounds_won"] - stats["rounds_lost"]
                writer.writerow([
                    team,
                    stats["matches_played"],
                    stats["wins"],
                    stats["losses"],
                    stats["rounds_won"],
                    stats["rounds_lost"],
                    rd,
                ])

        # Write match summary
        match_summary_path = os.path.join(base_dir, "match_summary.csv")

        def sort_key(m: Any) -> int:
            try:
                return int(m.match_id)
            except Exception:
                return 0
                
        with open(match_summary_path, 'w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["match_id","round","bracket","team1","team2","winner","loser","final_score","total_rounds"])

            for m in sorted(matches, key=sort_key):
                writer.writerow([
                    m.match_id,
                    m.round,
                    m.bracket,
                    m.team1,
                    m.team2,
                    m.winner,
                    m.loser,
                    m.final_score,
                    m.total_rounds,
                    ])
                
    # Single elimination simulation

    def run_single_elimination(self, tournament: Tournament) -> Dict[str, Any]:
        """
        Runs a full single-elimination tournament.
        16 -> 8 -> 4 -> 2 -> 1
        Automatically generates matches, simulates them,
        and exports full results to CSV.
        """
        tid = tournament.tournament_id
        tname = tournament.name

        # Ensure R1 matches exist
        r1 = self._get_matches(tid, "SE", 1)
        if not r1:
            teams = tournament.teams.copy()
            random.shuffle(teams)

            for i in range(0, 16, 2):
                self.match_manager.create_tournament_match(
                    team1=teams[i],
                    team2=teams[i+1],
                    bracket="SE",
                    round_number=1,
                    tournament_id=tid,
                    tournament_name = tname,
                )
            r1 = self._get_matches(tid, "SE", 1)

        # Simulate Round 1: 16 -> 8
        self._simulate_round(tid, "SE", 1)
        winners_r1 = [m.winner for m in self._get_matches(tid, "SE", 1)]

        # Generate Round 2: 8 -> 4
        r2 = self._get_matches(tid, "SE", 2)
        if not r2:
            for i in range(0, 8, 2):
                self.match_manager.create_tournament_match(
                    team1=winners_r1[i],
                    team2=winners_r1[i+1],
                    bracket="SE",
                    round_number=2,
                    tournament_id=tid,
                    tournament_name = tname,
                )

        # Simulate Round 2
        self._simulate_round(tid, "SE", 2)
        winners_r2 = [m.winner for m in self._get_matches(tid, "SE", 2)]

        # Generate Semifinals: 4 -> 2
        r3 = self._get_matches(tid, "SE", 3)
        if not r3:
            self.match_manager.create_tournament_match(
                team1=winners_r2[0],
                team2=winners_r2[1],
                bracket="SE",
                round_number=3,
                tournament_id=tid,
                tournament_name = tname,
            )
            self.match_manager.create_tournament_match(
                team1=winners_r2[2],
                team2=winners_r2[3],
                bracket="SE",
                round_number=3,
                tournament_id=tid,
                tournament_name = tname,
            )
        
        # Simulate Semifinals
        self._simulate_round(tid, "SE", 3)
        winners_r3 = [m.winner for m in self._get_matches(tid, "SE", 3)]

        # Generate Final: 2 -> 1
        final = self._get_matches(tid, "SE", 4)
        if not final:
            self.match_manager.create_tournament_match(
                team1=winners_r3[0],
                team2=winners_r3[1],
                bracket="SE",
                round_number=4,
                tournament_id=tid,
                tournament_name = tname,
            )
        
        # Simulate Final
        self._simulate_round(tid, "SE", 4)
        final_match = self._get_matches(tid, "SE", 4)[0]
        final_match = self.match_manager.repo.get_by_match_id(final_match.match_id)

        summary: Dict[str, Any] = {
            "champion": final_match.winner,
            "runner_up": final_match.loser,
            "final_score": final_match.final_score,
            "total_rounds": final_match.total_rounds,
        }

        self.export_full_results(tournament, summary)
        return summary