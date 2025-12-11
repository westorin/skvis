class Team:
    def __init__(self, team_id, name, captain, players, website_url, tag="", wins=0, losses=0):
        self.team_id = team_id
        self.name = name
        self.captain = captain
        self.players = players
        self.website_url = website_url
        self.tag = tag
        self.wins = wins
        self.losses = losses