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
    def __init__(self):
        self.players = PlayerRepository()
        self.teams = TeamRepository()
        self.tournaments = TournamentRepository()
        self.matches = MatchRepository()
        self.clubs = ClubRepository()
        self.passwords = PasswordRepository()
        self.roles = RoleRepository()