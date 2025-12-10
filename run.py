from main.UI.mainUI import MainUI
from main.UI.homepage_UI import homepageUI 
from main.UI.pickTimeOfTournament import PickTimeOfTournamentUI
from main.UI.leaderboard import LeaderBoardUI
from main.UI.listOfTeams import ListOfTeamsUI
from main.UI.listOfClubs import listOfClubsUI
from main.UI.login import LoginUI
from main.UI.listOfPlayers import ListOfPlayersUI
from main.UI.addtournament import AddTournamentUI
from main.UI.search import SearchUI
from main.UI.team import TeamUI
from main.UI.teamAllInfo import TeamAllInfoUI
from main.UI.pastTournamentsList import PastTournamentsUI
from main.UI.addTeam import AddTeamUI
from main.UI.pickLeaderBoard import PickLeaderBoardUI


run_program = MainUI(homepageUI, 
                     PickTimeOfTournamentUI, 
                     LeaderBoardUI, 
                     ListOfTeamsUI, 
                     listOfClubsUI, 
                     LoginUI, 
                     ListOfPlayersUI, 
                     AddTournamentUI, 
                     SearchUI, 
                     TeamUI, 
                     TeamAllInfoUI, 
                     PastTournamentsUI, 
                     AddTeamUI, 
                     PickLeaderBoardUI)
run_program.run()
