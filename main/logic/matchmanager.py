from main.repo.matchrepo import MatchRepository
from main.models.matchmodel import Match
import csv
import os
import random

class MatchManager:
    """Match creation and updates."""

    def __init__(self, match_repo: MatchRepository | None = None) -> None:
        self.repo = match_repo or MatchRepository()
    
    def create_match(self, data) -> Match:
        """Create a new match."""
        server_id = data["server_id"]

        if self.repo.get_by_server_id(server_id):
            raise ValueError("Server ID must be unique for each match")

        if data["team1"] == data["team2"]:
            raise ValueError("A team cannot play against itself")

        match = Match(
            date=data["date"],
            time=data["time"],
            server_id=server_id,
            team1=data["team1"],
            team2=data["team2"],
            score1=data.get("score1", 0),
            score2=data.get("score2", 0),
            winner=data.get("winner"),
            round=data.get("round"),
            tournament=data.get("tournament"),
        )

        self.repo.add_match(match)
        return match

    def create_tournament_match(self, team1, team2, bracket, round_number, tournament_id, tournament_name):
        match_id = self.repo.get_next_id()
        
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

    def list_matches(self):
        return self.repo.get_all()

    def set_scores(self, server_id, score1, score2, winner=None):
        updated = self.repo.update_scores(server_id, score1, score2, winner)
        if updated is None:
            raise ValueError("Match not found")
        return updated

    def _simulate_rounds(self,match_id):
        match = self.repo.get_by_match_id(match_id)

        team1 = match.team1
        team2 = match.team2

        t1_rounds = 0
        t2_rounds = 0
        round_number = 1
        round_logs = []

        #Regulation + win-by-2 OT
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
            
            #Overtime: win by 2
            if t1_rounds >= 12 and t2_rounds >= 12:
                if abs(t1_rounds - t2_rounds) >= 2:
                    break

            round_number += 1

        final_winner = team1 if t1_rounds > t2_rounds else team2
        final_loser = team2 if final_winner == team1 else team1
        total_rounds = t1_rounds + t2_rounds
        final_score = f"{t1_rounds}-{t2_rounds}"

        return final_winner, final_loser, total_rounds, final_score, round_logs

    def automate_all_matches(self):
        all_matches = self.repo.get_all()
        for match in all_matches:
            if match.winner is None:
                self.play_match_random(match.match_id)

        self.repo.save_to_file()
        return all_matches

    #Simulate random rounds, first to 13 wins
    def play_match_random(self,match_id):
        match = self.repo.get_by_match_id(match_id)

        if match is None:
            raise ValueError("Match not found")
        winner, loser, total_rounds, final_score, round_logs = self._simulate_rounds(match_id)

        match.winner = winner
        match.loser = loser
        match.final_score = final_score
        match.total_rounds = total_rounds

        # --- Folder creation chain (correct order) ---
        tname = match.tournament_name
        if not tname:
            tname = str(match.tournament_id)

        # Tournament folder
        tournament_folder = f"main/IO/{tname}"
        os.makedirs(tournament_folder, exist_ok=True)

        # Individual match folder
        match_folder = f"{tournament_folder}/match_{match.match_id}"
        os.makedirs(match_folder, exist_ok=True)

        print("Match folder created:", os.path.abspath(match_folder))

        #Write round files
        for rnum, rwinner in round_logs:
            round_path = f"{match_folder}/round_{rnum}.csv"
            with open(round_path, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["round", "winner"])
                writer.writerow([rnum, rwinner])
        
        #Write match_results.csv
        result_path = f"{match_folder}/match_results.csv"
        with open(result_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["match_id","team1","team2","winner","loser","final_score","total_rounds"])
            writer.writerow([match.match_id, match.team1, match.team2, winner, loser, final_score, total_rounds])

        self.repo.save_to_file()
        return match

    def simulate_round(self, matches):
        for m in matches:
            if m.winner is None:
                self.play_match_random(m.match_id)
        self.repo.save_to_file()

    def get_winner(self, match_id):
        match = self.repo.get_by_match_id(match_id)
        return match.winner

    def get_loser(self, match_id):
        match = self.repo.get_by_match_id(match_id)
        return match.loser

    def create_and_play(self,team1,team2,bracket,round_number,tournament_id):
        match = self.create_tournament_match(team1=team1,team2=team2,bracket=bracket,round_number=round_number,tournament_id=tournament_id)
        return self.play_match_random(match.match_id)

    def get_unfinished_matches(self):
        return [m for m in self.repo.get_all() if m.winner is None]
    
    def unfinished_in_round(self, matches):
        return [m for m in matches if m.winner is None]

    #round-by-round manual score input
    def play_match_manual(self,match_id):
        pass

    #Update CSV, team stats, bracket advancement
    def finalize_match(self,winner,loser):
        pass