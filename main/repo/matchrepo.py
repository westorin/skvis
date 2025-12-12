from typing import List, Optional

from main.IO.IOpy.matchIO import MatchIO
from main.models.matchmodel import Match
from main.IO.IOpy.matchtestIO import MatchTestIO
from main.models.matchtestmodel import MatchTestModel


class MatchRepository:
    """Repository responsible for loading, storing and persisting Match objects.
    Data is loaded from CSV on initialization and written back on updates."""
    def __init__(self) -> None:
        self.io = MatchIO()
        self.matches = self.load_matches()

    # Internal helpers

    def load_matches(self) -> List[Match]:
        """Load matches from CSV and convert them into Match objects."""
        rows = self.io.read_file()
        matches: List[Match] = []

        if not rows:
            return matches

        header = rows[0]
        data_rows = rows[1:] if header and header[0] == "match_id" else rows

        for row in data_rows:
            if not row:
                continue

            (
                match_id,
                team1,
                team2,
                date,
                time,
                server_id,
                round_name,
                bracket,
                winner,
                loser,
                tournament_id,
                final_score,
                total_rounds,
                score1,
                score2,
            ) = row

            if bracket == "W":
                bracket = "WB"
            elif bracket == "L":
                bracket = "LB"

            match = Match(
                match_id=match_id,
                team1=team1,
                team2=team2,
                date=date,
                time=time,
                server_id=server_id,
                round=round_name or None,
                bracket=bracket or None,
                winner=winner or None,
                loser=loser or None,
                tournament_id=tournament_id or None,
                final_score=final_score or None,
                total_rounds=int(total_rounds) if total_rounds else 0,
                score1=int(score1) if score1 else 0,
                score2=int(score2) if score2 else 0,
            )
            matches.append(match)

        return matches

    def save_to_file(self) -> None:
        """Persist all matches back to the CSV file."""
        rows = [
            [
                "match_id",
                "team1",
                "team2",
                "date",
                "time",
                "server_id",
                "round",
                "bracket",
                "winner",
                "loser",
                "tournament_id",
                "final_score",
                "total_rounds",
                "score1",
                "score2",
            ]
        ]

        for m in self.matches:
            rows.append(
                [
                    m.match_id,
                    m.team1,
                    m.team2,
                    m.date,
                    m.time,
                    m.server_id,
                    m.round or "",
                    m.bracket or "",
                    m.winner or "",
                    m.loser or "",
                    m.tournament_id or "",
                    m.final_score or "",
                    m.total_rounds,
                    m.score1,
                    m.score2,
                ]
            )

        self.io.write_file(rows)

    # Public API

    def add_match(self, match: Match) -> None:
        self.matches.append(match)
        self.save_to_file()

    def get_all(self) -> List[Match]:
        """Return a copy of all matches."""
        return list(self.matches)

    def get_by_server_id(self, server_id: str) -> Optional[Match]:
        """Find a match by server ID."""
        for m in self.matches:
            if str(m.server_id) == str(server_id):
                return m
        return None

    def update_scores(self, server_id: str, score1: int, score2: int, winner: Optional[str] = None) -> Optional[Match]:
        """Update scores for a match identified by server ID."""
        match = self.get_by_server_id(server_id)
        if match is None:
            return None

        match.score1 = int(score1)
        match.score2 = int(score2)
        match.winner = winner
        self.save_to_file()
        return match

    def get_by_match_id(self, match_id: str) -> Optional[Match]:
        """Find a match by match ID."""
        for m in self.matches:
            if str(m.match_id) == str(match_id):
                return m
        return None
    
    def get_next_id(self) -> int:
        """Return the next available match ID."""
        if not self.matches:
            return 1
        return max(int(m.match_id) for m in self.matches) + 1
    
    def get_by_tournament(self, tournament_id: str) -> List[Match]:
        result: List[Match] = []
        for m in self.matches:
            if str(m.tournament_id) == str(tournament_id):
                result.append(m)
        return result

    def save_all(self) -> None:
        """Explicitly persist all matches to file."""
        self.save_to_file()
        