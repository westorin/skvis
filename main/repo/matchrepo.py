from main.IO.IOpy.matchIO import MatchIO

class MatchRepository:
    def __init__(self):
        self.io = MatchIO()
        self.match = self.load_match()

    def load_match(self):
        rows = self.io.read_file()
        matches = []

        if not rows:
            return matches
        
        # header = rows[0]
        # data_rows = rows[1:]

        for row in rows:
            if not row:
                continue

            ( 
                date,
                time,
                server_id,
                team1,
                team2,
                score1,
                score2,
                winner,
                round,
                tournament,
            ) = row

            match = Match(
                date=date,
                time=time,
                server_id=server_id,
                team1=team1,
                team2=team2,
                score1=score1,
                score2=score2,
                winner=winner or None,
                round=round,
                tournament=tournament,
            )
            matches.append(match)
        
        return matches
    
    def save_to_file(self, Match) -> None: # Breyta nafni - save_match
        rows = []

        rows.append([
            "date",
            "time",
            "server_id",
            "team1",
            "team2",
            "score1",
            "score2",
            "winner",
            "round",
            "tournament",
        ])

        for m in self.matches:
            rows.append([
                m.date,
                m.time,
                m.server_id,
                m.team1,
                m.team2,
                m.score1,
                m.score2,
                m.winner or "",
                m.round,
                m.tournament,
            ])
        
        self.io.write_file(rows)

    def add_match(self, Match) -> None:
        self.matches.append(match)
        self.save_to_file()
    
    def get_all(self) -> Match:
        return list(self.tournaments)
    
    def get_by_server_ID(self, server_id) -> Match | None:
        for m in self.matches:
            if m.server_id == server_id:
                return m
        return None