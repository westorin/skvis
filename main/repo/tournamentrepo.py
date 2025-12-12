from typing import List, Optional

from main.IO.IOpy.tournamentIO import TournamentIO
from main.models.tournamentmodel import Tournament


class TournamentRepository:
    """Repository responsible for loading, storing and persisting Tournament objects."""
    def __init__(self) -> None:
        self.io = TournamentIO()
        self.tournaments: List[Tournament] = self.load_from_file()

    # Internal helpers

    def load_from_file(self) -> List[Tournament]:
        """Load tournaments from CSV and convert them into Tournament objects."""
        rows = self.io.read_file()
        tournaments: List[Tournament] = []

        if not rows:
            return tournaments

        # Skip header row
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
                tournament_id: Optional[int] = None

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
                try:
                    tournament_id = int(tournament_id)
                except (TypeError, ValueError):
                    tournament_id = None

            else:
                continue
            
            # Stored as pipe-seperated strings in CSV
            teams: List[str] = teams.split("|") if teams else []
            matches: List[str] = matches.split("|") if matches else []

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
        """Persist all tournaments back to the CSV file."""
        rows: List[list[str]] = []

        # Header row
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

            tournament_id_value = str(t.tournament_id) if t.tournament_id is not None else ""

            rows.append([
                tournament_id_value,
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

    # Public API

    def add_tournament(self, tournament: Tournament) -> None:
        """Add a new tournament and persist it."""
        self.tournaments.append(tournament)
        self.save_to_file()

    def get_all(self) -> List[Tournament]:
        """Return a copy of all tournaments."""
        return list(self.tournaments)

    def get_by_name(self, name: str) -> Optional[Tournament]:
        """Find a tournament by name."""
        for t in self.tournaments:
            if t.name.lower() == name.lower():
                return t
        return None
    
    def get_by_id(self, tournament_id: int) -> Optional[Tournament]:
        """Find a tournament by its numeric ID."""
        for t in self.tournaments:
            if t.tournament_id == tournament_id:
                return t
        return None
    
    def get_next_id(self) -> int:
        """Return the next available tournament ID."""
        if not self.tournaments:
            return 1
        
        id_values: List[int] = []
        for t in self.tournaments:
            try:
                if t.tournament_id is not None:
                    id_values.append(int(t.tournament_id))
            except (TypeError, ValueError):
                continue

        if not id_values:
            return 1

        max_id = max(id_values)
        return max_id + 1
    
    def save(self) -> None:
        """Convenience method used by managers. This just persists the current in-memory tournaments list to CSV."""
        self.save_to_file()

    def update_tournament(self, tournament: Tournament) -> None:
        """Replace an existing tournament (matched by tournament_id) and persist changes."""
        for idx, t in enumerate(self.tournaments):
            if t.tournament_id == tournament.tournament_id:
                self.tournaments[idx] = tournament
                self.save_to_file()
                return
            
    def get_tournament(self, tournament_name: str) -> Optional[Tournament]:
        """Alias for get_by_name (kept for compatibility with older code)."""
        return self.get_by_name(tournament_name)
