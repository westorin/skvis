#LogicWrapper
from main.logic.playermanager import PlayerManager
from main.logic.teammanager import TeamManager
from main.logic.tournamentmanager import TournamentManager
from main.logic.matchmanager import MatchManager
from main.logic.searchmanager import SearchManager
from main.logic.loginmanager import LoginManager
#from main.logic.clearScreenInTerminal import clear_screen

class LogicWrapper:
    def __init__(self, data):
        self.player_manager = PlayerManager(data.players)
        self.team_manager = TeamManager(data.teams, data.players)
        self.player_manager.team_manager = self.team_manager  # Link TeamManager to PlayerManager

        #self.tournament_manager = TournamentManager(data.tournaments, data.teams)

        #self.match_manager = MatchManager(data.matches)
        #self.search_manager = SearchManager(data.players,data.teams,data.tournaments)
        self.login_manager = LoginManager(data.players, data.roles, data.passwords)
