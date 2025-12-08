from main.models.teammodel import Team
from main.IO.IOpy.teamIO import TeamIO

class TeamRepository:
    def __init__(self):
        self.io = TeamIO()
        self.teams = self.load_teams()

    # Load teams from storage
    def load_teams(self):
        rows = self.io.read_file()
        teams = []
        for row in rows:
            if row[0] == 'team_id':
                continue  # Skip header row
            else:
                team_id = row[0]
                name = row[1]
                captain = row[2]
                players = row[3].split("|") if row[3] else []
                website_url = row[4]

                t = Team(team_id, name, captain, players, website_url,wins=0,losses=0)
                teams.append(t)

        return teams

    # Save teams to storage
    def save_teams(self):
        rows = [["team_id", "name", "captain", "players", "website_url"]]
        for t in self.teams:
            player_string = "|".join(t.players)
            rows.append([
                t.team_id,
                t.name,
                t.captain,
                player_string,
                t.website_url
            ])
        self.io.write_file(rows)

    # Add a new team
    def add_team(self, team):
        self.teams.append(team)
        self.save_teams()

    # Get the next available team ID
    def get_next_id(self):
        if not self.teams:
            return 1
        else:
            max_id = max(int(team.team_id) for team in self.teams)
            return max_id + 1
    
    # Get team by name
    def get_team(self, team_name):
        for team in self.teams:
            n = team.name
            if n.lower() == team_name:
                return team
        return None
    
    def get_all_players_in_team(self) -> list:
        all_players = []
        for team in self.teams:
            for player in team.players:
                all_players.append(player)
        return all_players