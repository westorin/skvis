from main.logic.matchmanager import MatchManager
from main.logic.tournamentmanager import TournamentManager
from main.repo.matchrepo import MatchRepository
from main.repo.playerrepo import PlayerRepository
from main.repo.teamrepo import TeamRepository
from main.repo.tournamentrepo import TournamentRepository
from main.repo.matchrepo import MatchRepository
from main.repo.clubrepo import ClubRepository
from main.repo.passwordrepo import PasswordRepository
from main.repo.rolesrepo import RoleRepository

class DataWrapper:
    """Holds repository instances (data access layer)."""
    def __init__(self) -> None:
        self.players: PlayerRepository = PlayerRepository()
        self.teams: TeamRepository = TeamRepository()
        self.tournaments: TournamentRepository = TournamentRepository()
        self.matches: MatchRepository = MatchRepository()
        self.clubs: ClubRepository = ClubRepository()
        self.passwords: PasswordRepository = PasswordRepository()
        self.roles: RoleRepository = RoleRepository()
