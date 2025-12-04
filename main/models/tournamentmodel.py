class Tournament:
    def __init__(
        self,
        name,
        start,
        end,
        location,
        contact_email,
        contact_phone,
        teams=None,
        matches=None,
        winner=None,
        tournament_id=None,
    ):
        self.tournament_id = tournament_id
        self.name = name
        self.start = start
        self.end = end
        self.location = location
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.teams = teams or []
        self.matches = matches or []
        self.winner = winner
