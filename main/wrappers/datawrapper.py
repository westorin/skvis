#DataWrapper = (Repositories) → IO → CSV
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

        self.match_manager = MatchManager(self.matches)
        self.tournament_manager = TournamentManager(self.tournaments, 
                                                    self.teams, 
                                                    self.match_manager)

        self.clubs = ClubRepository()
        self.passwords = PasswordRepository()
        self.roles = RoleRepository()

