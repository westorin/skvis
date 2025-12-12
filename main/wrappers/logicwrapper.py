# LogicWrapper
from main.logic.playermanager import PlayerManager
from main.logic.teammanager import TeamManager
from main.logic.tournamentmanager import TournamentManager
from main.logic.matchmanager import MatchManager
from main.logic.loginmanager import LoginManager
from main.logic.clearScreenInTerminal import ClearScreenLogic
from main.logic.leaderboardmanager import LeaderboardManager
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from main.wrappers.datawrapper import DataWrapper

class LogicWrapper:
    def __init__(self, data) -> None:
        self.data = data
        self.clear_screen = ClearScreenLogic() 
        self.player_manager: PlayerManager = PlayerManager(data.players)
        self.team_manager: TeamManager = TeamManager(data.teams, data.players, data.passwords)

        # PlayerManager needs TeamManager for syncing username/team changes
        self.player_manager.team_manager = self.team_manager

        self.match_manager: MatchManager = MatchManager(data.matches)

        self.tournament_manager: TournamentManager = TournamentManager(
            data.tournaments,
            data.teams,
            self.match_manager,
        )

        # Authentication / roles
        self.login_manager: LoginManager = LoginManager(data.players, data.roles, data.passwords)

        # Leaderboard logic depends on matches + teams + tournaments
        self.leaderboard_manager: LeaderboardManager = LeaderboardManager(data)
