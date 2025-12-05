class Match:
    def __init__(
        self,
        date,
        time,
        server_id,
        team1,
        team2,
        score1=0,
        score2=0,
        winner=None,
        round=None,
        tournament=None,
    ):
        self.date = date
        self.time = time
        self.server_id = server_id
        self.team1 = team1
        self.team2 = team2
        self.score1 = int(score1) if score1 != "" else 0
        self.score2 = int(score2) if score2 != "" else 0
        self.winner = winner
        self.round = round
        self.tournament = tournament
