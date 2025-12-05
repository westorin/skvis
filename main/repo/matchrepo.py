from main.IO.IOpy.matchIO import MatchIO
from main.models.matchmodel import Match


class MatchRepository:
    def __init__(self):
        self.io = MatchIO()
        self.matches = self.load_matches()

    # internal helpers

    def load_matches(self):
        rows = self.io.read_file()
        matches = []

        if not rows:
            return matches

        header = rows[0]
        data_rows = rows[1:] if header and header[0] == "date" else rows

        for row in data_rows:
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
                round_name,
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
                round=round_name or None,
                tournament=tournament or None,
            )
            matches.append(match)

        return matches

    def save_to_file(self) -> None:
        rows = [
            [
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
            ]
        ]

        for m in self.matches:
            rows.append(
                [
                    m.date,
                    m.time,
                    m.server_id,
                    m.team1,
                    m.team2,
                    m.score1,
                    m.score2,
                    m.winner or "",
                    m.round or "",
                    m.tournament or "",
                ]
            )

        self.io.write_file(rows)

    # public methods

    def add_match(self, match: Match) -> None:
        self.matches.append(match)
        self.save_to_file()

    def get_all(self):
        return list(self.matches)

    def get_by_server_id(self, server_id):
        for m in self.matches:
            if str(m.server_id) == str(server_id):
                return m
        return None

    def update_scores(self, server_id, score1, score2, winner=None):
        match = self.get_by_server_id(server_id)
        if match is None:
            return None

        match.score1 = int(score1)
        match.score2 = int(score2)
        match.winner = winner
        self.save_to_file()
        return match
