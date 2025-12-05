from main.repo.matchrepo import MatchRepository
from main.models.matchmodel import Match

class MatchManager:
    """Coordinates match creation and updates."""

    def __init__(self) -> None:
        self.repo = MatchRepository()
    
    def create_match(self, data) -> Match:
        """Create and persist a new match."""
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

    def list_matches(self):
        return self.repo.get_all()

    def set_scores(self, server_id, score1, score2, winner=None):
        updated = self.repo.update_scores(server_id, score1, score2, winner)
        if updated is None:
            raise ValueError("Match not found")
        return updated
