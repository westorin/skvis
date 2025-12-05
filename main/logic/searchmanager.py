class SearchManager:
    def __init__(self, player_manager, team_manager):
        self.player_manager = player_manager
        self.team_manager = team_manager

    def search_players_by_name(self, name_query):
        matching_players = []
        for player in self.player_manager.get_all_players():
            if name_query.lower() in player.name.lower():
                matching_players.append(player)
        return matching_players

    def search_teams_by_name(self, name_query):
        matching_teams = []
        for team in self.team_manager.get_all_teams():
            if name_query.lower() in team.name.lower():
                matching_teams.append(team)
        return matching_teams