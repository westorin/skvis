from typing import List, Optional # Má nota optional?
from main.IO.IOpy.tournamentIO import TournamentIO
from main.models.tournamentmodel import Tournament


class TournamentRepository:
    def __init__(self) -> None:
        self.io = TournamentIO()
        self.tournaments: List[Tournament] = self.load_from_file()

    # internal helpers

    def load_from_file(self) -> List[Tournament]:
        rows = self.io.read_file()
        tournaments: List[Tournament] = []

        if not rows:
            return tournaments

        data_rows = rows[1:]

        for row in data_rows:
            if not row:
                continue
            
            if len(row) == 9:
                (
                    name,
                    start,
                    end,
                    location,
                    contact_email,
                    contact_phone,
                    teams,
                    matches,
                    winner,
                ) = row
                tournament_id = None

            elif len(row) == 10:
                (
                    tournament_id,
                    name,
                    start,
                    end,
                    location,
                    contact_email,
                    contact_phone,
                    teams,
                    matches,
                    winner,
                ) = row

            else:
                continue

            teams = teams.split("|") if teams else []
            matches = matches.split("|") if matches else []

            tournament = Tournament(
                name=name,
                start=start,
                end=end,
                location=location,
                contact_email=contact_email,
                contact_phone=contact_phone,
                teams=teams,
                matches=matches,
                winner=winner or None,
                tournament_id=tournament_id if tournament_id else None,
            )
            tournaments.append(tournament)

        return tournaments

    def save_to_file(self) -> None:
        rows: List[list[str]] = []

        rows.append([
            "tournament_id",
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

        for t in self.tournaments:
            # Convert lists back to strings seperated by pipes
            if t.teams:
                teams = "|".join(t.teams)
            else:
                teams = ""
            
            
            if t.matches:
                matches = "|".join([str(m) for m in t.matches])
            else:
                matches = ""

            rows.append([
                str(t.tournament_id),
                t.name,
                t.start,
                t.end,
                t.location,
                t.contact_email,
                t.contact_phone,
                teams,
                matches,
                t.winner or "",
            ])

        self.io.write_file(rows)

    # public methods

    def add_tournament(self, tournament: Tournament) -> None:
        self.tournaments.append(tournament)
        self.save_to_file()

    def get_all(self) -> List[Tournament]:
        return list(self.tournaments)

    def get_by_name(self, name: str) -> Optional[Tournament]:
        for t in self.tournaments:
            if t.name == name:
                return t
        return None
    
    def get_next_id(self) -> int:
        if not self.tournaments:
            return 1
        max_id = max(t.tournament_id or 0 for t in self.tournaments)
        return max_id + 1
    
    def save(self) -> None:
        """ - """ # Comment her
        self.save_to_file()