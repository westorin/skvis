class Match:
    def __init__(
        self,
        match_id,
        team1,
        team2,
        date=None,
        time=None,
        server_id=None,
        round=None,
        bracket=None,
        winner=None,
        loser=None,
        tournament_id=None,
        final_score=None,
        total_rounds=0,
        score1=0,
        score2=0,
    ):
        self.match_id = match_id
        self.team1 = team1
        self.team2 = team2
        self.date = date
        self.time = time
        self.server_id = server_id
        self.round = round
        self.bracket = bracket
        self.winner = winner
        self.loser = loser
        self.tournament_id = tournament_id
        self.final_score = final_score
        self.total_rounds = total_rounds
        self.score1 = int(score1) if score1 != "" else 0
        self.score2 = int(score2) if score2 != "" else 0