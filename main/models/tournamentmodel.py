class Tournament:
    def __init__(self, tournament_id, name, start, end, location, contact_email, contact_phone, teams, matches, winner):
        self.tournament_id = tournament_id
        self.name = name
        self.start = start
        self.end = end
        self.location = location
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.teams = teams
        self.matches = matches
        self.winner = winner