from typing import List, Optional

from main.models.teammodel import Team
from main.IO.IOpy.teamIO import TeamIO

class TeamRepository:
    """Repository responsible for loading, storing and retrieving Team objects."""
    def __init__(self) -> None:
        self.io = TeamIO()
        self.teams: List[Team] = self.load_teams()

    # Loading / Saving

    def load_teams(self) -> List[Team]:
        """Load teams from CSV and convert them into Team objects."""
        rows = self.io.read_file()
        teams: List[Team] = []

        for row in rows:
            if row[0] == 'team_id':
                continue  # Skip header row

            team_id = row[0]
            name = row[1]
            captain = row[2]
            players = row[3].split("|") if row[3] else []
            website_url = row[4]
            tag = row[5] if len(row) > 5 else ""

            t = Team(team_id, name, captain, players, website_url, tag, wins=0, losses=0)
            teams.append(t)

        return teams

    def save_teams(self) -> None:
        rows = [["team_id", "name", "captain", "players", "website_url"]]
        for t in self.teams:
            player_string = "|".join(t.players)
            rows.append([
                t.team_id,
                t.name,
                t.captain,
                player_string,
                t.website_url,
                t.tag,
            ])
        self.io.write_file(rows)

    # Public API

    def add_team(self, team: Team) -> None:
        """Add a new team and persist the change."""
        self.teams.append(team)
        self.save_teams()

    def get_next_id(self) -> int:
        """Return the next available team ID."""
        if not self.teams:
            return 1
        return max(int(team.team_id) for team in self.teams) + 1
    
    def get_team(self, team_name: str) -> Optional[Team]:
        """Retrieve a team by name"""
        for team in self.teams:
            n = team.name
            if n.lower() == team_name.lower():
                return team
        return None
    
    def get_all_players_in_team(self) -> List[str]:
        """Return a flat list of all player username accross all teams."""
        all_players: List[str] = []
        for team in self.teams:
            for player in team.players:
                all_players.append(player)
        return all_players
    
    def get_all(self) -> List[Team]:
        """Return a copy of all teams."""
        return list(self.teams)