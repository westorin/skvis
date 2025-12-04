from main.repo.teamrepo import TeamRepository
from main.repo.playerrepo import PlayerRepository
from main.models.teammodel import Team

class TeamManager:
    def __init__(self):
        self.team_repo = TeamRepository()
        self.player_repo = PlayerRepository()

    # Create a new team
    def register_team(self, name, captain_handle, website_url="") -> "Team":
        team_id = self.team_repo.get_next_id()

        # Look up captain by name
        captain = self.player_repo.get_by_handle(captain_handle)
        if captain is None:
            print("DEBUG PLAYERS:", [(p.username) for p in self.player_repo.players])
            raise ValueError("Captain must be a registered player")
            

        # Team name must be unique
        if self.team_repo.get_team(name):
            raise ValueError("Team name must be unique")

        new_team = Team(
            team_id=team_id,
            name=name,
            captain=captain_handle,
            players=[captain_handle],
            website_url=website_url
        )

        # Add team to repository
        self.team_repo.add_team(new_team)

        # Assign captain to the team
        captain.team = name
        self.player_repo.save_players()

        return new_team

    # Add a player to a team
    def add_player_to_team(self, team_name, player_handle):
        team = self.team_repo.get_team(team_name)
        if team is None:
            raise ValueError("Team does not exist")

        # Look up player object by name
        player = self.player_repo.get_by_handle(player_handle)
        if player is None:
            raise ValueError("Player does not exist")

        if player.team == team_name:
            raise ValueError("Player is already in the team")

        # Max team size = 5
        if len(team.players) >= 5:
            print("DEBUG team.players =", team.players, type(team.players))
            raise ValueError("Team is already full (max 5 players)")

        # Add player to team
        team.players.append(player_handle)
        player.team = team_name

        # Save updates
        self.team_repo.save_teams()
        self.player_repo.save_players()

        return team