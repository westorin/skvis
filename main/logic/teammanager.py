from typing import List, Dict # Type hinting
from main.repo.teamrepo import TeamRepository

class TeamManager:
    """Handles creating and storing teams in memory."""

    def __init__(self) -> None:
        self.repo = TeamRepository()

    def create_team(self, data: Dict) -> Dict:
        """Creates a new team and stores it in the list"""

        name = data["name"]

        if self.get_team(name) is not None:
            raise ValueError("Team name must be unique")
        
        team: Dict = {
            "name": name,
            "captain": data["captain"],
            "players": data["players"],
            "website_url": data["website_url"],
        }

        self.repo.add_team(team)

        return team
    
    def get_team(self, name: str) -> Dict | None:
        """Return team with this name, or None."""
        return self.repo.get_by_team_name(name)

    def list_teams(self) -> List[Dict]:
        """Return list of all teams"""
        return self.repo.get_all()