# main/models/tournamentmodel.py

class Tournament:
    def __init__(
        self,
        name: str,
        start_date: str,
        end_date: str,
        location: str,
        contact_email: str,
        contact_phone: str,
        teams: list | None = None,
        matches: list | None = None,
        winner: str | None = None,
    ) -> None:
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.location = location
        self.contact_email = contact_email
        self.contact_phone = contact_phone
        self.teams = teams if teams is not None else []
        self.matches = matches if matches is not None else []
        self.winner = winner
