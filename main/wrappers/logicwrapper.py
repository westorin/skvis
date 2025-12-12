#LogicWrapper
from main.logic.playermanager import PlayerManager
from main.logic.teammanager import TeamManager
from main.logic.tournamentmanager import TournamentManager
from main.logic.matchmanager import MatchManager
from main.logic.loginmanager import LoginManager
#from main.logic.leaderboardmanager import LeaderboardManager
from main.logic.clearScreenInTerminal import ClearScreenLogic
from main.logic.leaderboardmanager import LeaderboardManager




class LogicWrapper:
    def __init__(self, data) -> None:
        self.data = data
        self.clear_screen = ClearScreenLogic() 
        self.player_manager: PlayerManager = PlayerManager(data.players)
        self.team_manager: TeamManager = TeamManager(data.teams, data.players, data.passwords)
        self.player_manager.team_manager = self.team_manager  # Link TeamManager to PlayerManager
        self.match_manager: MatchManager = MatchManager(data.matches)
        self.tournament_manager: TournamentManager = TournamentManager(
            data.tournaments,
            data.teams,
            self.match_manager
        )
        #self.search_manager: SearchManager = SearchManager(data.players, data.teams, data.tournaments)
        self.login_manager: LoginManager = LoginManager(data.players, data.roles, data.passwords)
        self.leaderboard_manager = LeaderboardManager(data)