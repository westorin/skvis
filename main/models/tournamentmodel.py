class Tournament:
    def __init__(self, tournament_id, name, start_date, end_date, location, contact_email, contact_phone, teams, matches, winner):
        self.tournament_id = tournament_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.teams = teams
        self.matches = matches
        self.winner = winner