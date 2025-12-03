from typing import List
from main.IO.tournamentIO import TournamentIO
from main.models.tournamentmodel import Tournament


class TournamentRepository:
    def __init__(self) -> None:
        self.io = TournamentIO()
        self._tournaments: List[Tournament] = self._load_from_file()

    # internal helpers

    def _load_from_file(self) -> List[Tournament]:
        rows = self.io.read_file()
        tournaments: List[Tournament] = []

        if not rows:
            return tournaments

        header = rows[0]
        data_rows = rows[1:]

        for row in data_rows:
            if not row:
                continue

            (
                name,
                start_date,
                end_date,
                location,
                contact_email,
                contact_phone,
                teams,
                matches,
                winner,
            ) = row

            tournament = Tournament(
                name=name,
                start_date=start_date,
                end_date=end_date,
                location=location,
                contact_email=contact_email,
                contact_phone=contact_phone,
                teams=[],      # not loading from CSV yet
                matches=[],    # same here
                winner=winner or None,
            )
            tournaments.append(tournament)

        return tournaments

    def _save_to_file(self) -> None:
        rows: List[list[str]] = []

        rows.append([
            "name",
            "start_date",
            "end_date",
            "location",
            "contact_email",
            "contact_phone",
            "teams",
            "matches",
            "winner",
        ])

        for t in self._tournaments:
            rows.append([
                t.name,
                t.start_date,
                t.end_date,
                t.location,
                t.contact_email,
                t.contact_phone,
                "",                   # teams serialisation later
                "",                   # matches serialisation later
                t.winner or "",
            ])

        self.io.write_file(rows)

    # public methods

    def add_tournament(self, tournament: Tournament) -> None:
        self._tournaments.append(tournament)
        self._save_to_file()

    def get_all(self) -> List[Tournament]:
        return list(self._tournaments)

    def get_by_name(self, name: str) -> Tournament | None:
        for t in self._tournaments:
            if t.name == name:
                return t
        return None
