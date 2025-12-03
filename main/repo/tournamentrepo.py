from typing import List, Dict
from main.IO.tournamentIO import TournamentIO


class TournamentRepository:
    def __init__(self) -> None:
        self.io = TournamentIO()
        self._tournaments: List[Dict] = self._load_from_file()

    # ------------ internal helpers ------------

    def _load_from_file(self) -> List[Dict]:
        rows = self.io.read_file()
        tournaments: List[Dict] = []

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

            tournaments.append({
                "name": name,
                "start_date": start_date,
                "end_date": end_date,
                "location": location,
                "contact_email": contact_email,
                "contact_phone": contact_phone,
                "teams": [],
                "matches": [],
                "winner": winner or None,
            })

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
                t["name"],
                t["start_date"],
                t["end_date"],
                t["location"],
                t["contact_email"],
                t["contact_phone"],
                "",  
                "",  
                t["winner"] or "",
            ])

        self.io.write_file(rows)

    # ------------ public API ------------

    def add_tournament(self, tournament: Dict) -> None:
        self._tournaments.append(tournament)
        self._save_to_file()

    def get_all(self) -> List[Dict]:
        return list(self._tournaments)

    def get_by_name(self, name: str) -> Dict | None:
        for t in self._tournaments:
            if t["name"] == name:
                return t
        return None
