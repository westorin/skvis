from main.repo.matchrepo import MatchRepository
from main.models.matchmodel import Match

import csv
import os
import random
from typing import Any, Optional, List, Tuple

class MatchManager:
    """Responsible for creating matches, updating results and simulating matches."""

    def __init__(self, match_repo: Optional[MatchRepository] = None) -> None:
        """match_repo: Optional repository injection for testing. If None, a new MatchRepository is created."""
        self.repo: MatchRepository = match_repo or MatchRepository()
    
    def create_match(self, data: dict[str, Any]) -> Match:
        """Create a new match from a data dictionary and store it in the repository."""
        server_id: str = data["server_id"]

        # Enforce unique server ID per match
        if self.repo.get_by_server_id(server_id): 
            raise ValueError("Server ID must be unique for each match")

        # Prevent a team playing against itself
        if data["team1"] == data["team2"]:
            raise ValueError("A team cannot play against itself")

        match = Match(
            match_id=self.repo.get_next_id(),
            team1=data["team1"],
            team2=data["team2"],
            date=data["date"],
            time=data["time"],
            server_id=server_id,
            round=data.get("round"),
            bracket=data.get("bracket"),
            winner=data.get("winner"),
            loser=data.get("loser"),
            tournament_id=data.get("tournament_id"),
            tournament_name=data.get("tournament_name"),
            final_score=data.get("final_score"),
            total_rounds=data.get("total_rounds", 0),
            score1=data.get("score1", 0),
            score2=data.get("score2", 0),
        )

        self.repo.add_match(match)
        return match

    def create_tournament_match(self, team1: str, team2: str, bracket: str, round_number: int, tournament_id: str, tournament_name: str) -> Match:
        """Create a match that belongs to a tournament bracket. This creates a unique server_id based on tournament_id and match_id"""
        match_id: int = self.repo.get_next_id()
        
        match = Match(
            match_id=match_id,
            team1=team1,
            team2=team2,
            date=None,
            time=None,
            server_id=f"{tournament_id}_match_{match_id}",
            round=round_number,
            bracket=bracket,
            winner=None,
            loser=None,
            tournament_id=tournament_id,
            tournament_name=tournament_name,
            final_score=None,
            total_rounds=0,
            score1=0,
            score2=0,
        )
        self.repo.add_match(match)
        return match

    def list_matches(self) -> List[Match]:
        """Return all matches from the repository."""
        return self.repo.get_all()

    def set_scores(self, server_id: str, score1: int, score2: int, winner: Optional[str] = None) -> Match:
        """Update scores (and optionally winner) for a match identified by server_id."""
        updated = self.repo.update_scores(server_id, score1, score2, winner)
        if updated is None:
            raise ValueError("Match not found")
        return updated

    def _simulate_rounds(self, match_id: int) -> Tuple[str, str, int, str, List[Tuple[int, str]]]:
        """Simulate a match round-by-round."""
        match = self.repo.get_by_match_id(match_id)
        if match is None:
            raise ValueError("Match not found")

        team1: str = match.team1
        team2: str = match.team2

        t1_rounds: int = 0
        t2_rounds: int = 0
        round_number: int = 1
        round_logs: List[Tuple[int, str]] = []

        #Regulation + overtime (win by 2 from 12-12)
        while True:
            winner = random.choice([team1,team2])
            loser = team2 if winner == team1 else team1
            if winner == team1:
                t1_rounds += 1
            else:
                t2_rounds += 1

            round_logs.append((round_number, winner))

            #Stop at 13 wins
            if t1_rounds == 13 or t2_rounds == 13:
                break
            
            #Overtime: win by 2 if both teams reached 12
            if t1_rounds >= 12 and t2_rounds >= 12:
                if abs(t1_rounds - t2_rounds) >= 2:
                    break

            round_number += 1

        final_winner = team1 if t1_rounds > t2_rounds else team2
        final_loser = team2 if final_winner == team1 else team1
        total_rounds = t1_rounds + t2_rounds
        final_score = f"{t1_rounds}-{t2_rounds}"

        return final_winner, final_loser, total_rounds, final_score, round_logs

    def _apply_result(self, match: Match, score1: int | str, score2: int | str) -> None:
        """Set winner/loser and score fields on a match."""
        s1 = int(score1)
        s2 = int(score2)

        if s1 < 0 or s2 < 0:
            raise ValueError("Scores must be non-negative")

        if s1 == s2:
            raise ValueError("Match cannot end in a draw. One team must win.")

        match.score1 = s1
        match.score2 = s2
        match.final_score = f"{s1}-{s2}"
        match.total_rounds = s1 + s2

        if s1 > s2:
            match.winner = match.team1
            match.loser = match.team2
        else:
            match.winner = match.team2
            match.loser = match.team1

    def set_match_result(self, match_id: int, score1: int, score2: int) -> Match:
        match = self.repo.get_by_match_id(match_id)

        if match is None:
            raise ValueError("Match not found")

        if match.winner is not None:
            raise ValueError("Match already has a result")

        # Apply scores + winner/loser
        self._apply_result(match, score1, score2)

        # Folder structure: main/IO/<tournament_name>/match_<id>
        tname = match.tournament_name if match.tournament_name else str(match.tournament_id)
        tournament_folder = f"main/IO/{tname}"
        os.makedirs(tournament_folder, exist_ok=True)

        match_folder = f"{tournament_folder}/match_{match.match_id}"
        os.makedirs(match_folder, exist_ok=True)

        # Write match_results.csv
        result_path = f"{match_folder}/match_results.csv"
        with open(result_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([
                "match_id",
                "team1",
                "team2",
                "winner",
                "loser",
                "final_score",
                "total_rounds",
            ])
            writer.writerow([
                match.match_id,
                match.team1,
                match.team2,
                match.winner,
                match.loser,
                match.final_score,
                match.total_rounds,
            ])

        self.repo.save_to_file()
        return match

    def automate_all_matches(self) -> List[Match]:
        """Automatically simulate all unfinished matches and persist results. Returns the full list of matches after automation."""
        all_matches = self.repo.get_all()
        for match in all_matches:
            if match.winner is None:
                self.play_match_random(match.match_id)

        self.repo.save_to_file()
        return all_matches

    def play_match_random(self, match_id: int) -> Match:
        """Simulate a match and write round logs + results to CSV files."""
        match = self.repo.get_by_match_id(match_id)
        if match is None:
            raise ValueError("Match not found")
        
        winner, loser, total_rounds, final_score, round_logs = self._simulate_rounds(match_id)

        match.winner = winner
        match.loser = loser
        match.final_score = final_score
        match.total_rounds = total_rounds

        # Determine tournament folder name
        tname = match.tournament_name
        if not tname:
            tname = str(match.tournament_id)

        # Create folders (tournament folder first, then match folder)
        tournament_folder = f"main/IO/{tname}"
        os.makedirs(tournament_folder, exist_ok=True)

        # Individual match folder
        match_folder = f"{tournament_folder}/match_{match.match_id}"
        os.makedirs(match_folder, exist_ok=True)

        # Write each simulated round to its own CSV file
        for rnum, rwinner in round_logs:
            round_path = f"{match_folder}/round_{rnum}.csv"
            with open(round_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["round", "winner"])
                writer.writerow([rnum, rwinner])
        
        # Write the match results summary CSV
        result_path = f"{match_folder}/match_results.csv"
        with open(result_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["match_id","team1","team2","winner","loser","final_score","total_rounds"])
            writer.writerow([match.match_id, match.team1, match.team2, winner, loser, final_score, total_rounds])

        self.repo.save_to_file()
        return match

    def simulate_round(self, matches: List[Match]) -> None:
        """Simlate all unfinished matches in the provided list and persist results."""
        for m in matches:
            if m.winner is None:
                self.play_match_random(m.match_id)
        self.repo.save_to_file()

    def get_winner(self, match_id: int) -> Optional[str]:
        """Return the winner team name for a match, or None if not decided."""
        match = self.repo.get_by_match_id(match_id)
        if match is None:
            return None
        return match.winner

    def get_loser(self, match_id):
        """Return the loser team name for a match, or None if not decided."""
        match = self.repo.get_by_match_id(match_id)
        if match is None:
            return None
        return match.loser

    def create_and_play(self, team1: str, team2: str, bracket: str, round_number: int, tournament_id: int) -> Match:
        """Convenience method: create a tournament match and immediately simulate it."""
        match = self.create_tournament_match(team1=team1,team2=team2,bracket=bracket,round_number=round_number,tournament_id=tournament_id, tournament_name="")
        return self.play_match_random(match.match_id)

    def get_unfinished_matches(self):
        """Return all matches that do not yet have a winner."""
        return [m for m in self.repo.get_all() if m.winner is None]
    
    def unfinished_in_round(self, matches: List[Match]) -> List[Match]:
        """Filter a list of matches down to only those without a winner."""
        return [m for m in matches if m.winner is None]

    def play_match_manual(self, match_id: int, score1: int | str, score2: int | str) -> Match:
        """Record a manual result for a match and write match_results.csv. This uses the same folder + output CSV behaviour as random simulation"""
        match = self.repo.get_by_match_id(match_id)
        if match is None:
            raise ValueError("Match not found")

        if match.winner is not None:
            raise ValueError("Result already registered for this match")

        # Update match object with scores + winner/loser
        self._apply_result(match, score1, score2)

        # Keep folder/result CSV behaviour consistent with random simulation
        tname = match.tournament_name if match.tournament_name else str(match.tournament_id)

        tournament_folder = f"main/IO/{tname}"
        os.makedirs(tournament_folder, exist_ok=True)

        match_folder = f"{tournament_folder}/match_{match.match_id}"
        os.makedirs(match_folder, exist_ok=True)

        result_path = f"{match_folder}/match_results.csv"
        with open(result_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["match_id", "team1", "team2", "winner", "loser", "final_score", "total_rounds"])
            writer.writerow([
                match.match_id,
                match.team1,
                match.team2,
                match.winner,
                match.loser,
                match.final_score,
                match.total_rounds,
            ])

        self.repo.save_to_file()
        return match

    #Update CSV, team stats, bracket advancement
    def finalize_match(self, winner: str, loser: str) -> None:
        """Placeholder for future work: update CSV/team stats/bracket advancement."""
        pass