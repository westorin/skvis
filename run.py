from main.UI.mainUI import MainUI
from main.UI.homepage_UI import homepageUI 
from main.UI.pickTimeOfTournament import PickTimeOfTournamntsUI
from main.UI.leaderboard import LeaderBoardUI
from main.UI.listOfTeams import ListOfTeamsUI
from main.UI.listOfClubs import listOfClubsUI
from main.UI.login import LoginUI
from main.UI.listOfPlayers import ListOfPlayersUI
from main.UI.addtournament import AddTournamentUI
from main.UI.search import SearchUI



run_program = MainUI(homepageUI, PickTimeOfTournamntsUI, LeaderBoardUI, ListOfTeamsUI, listOfClubsUI, LoginUI, ListOfPlayersUI, AddTournamentUI, SearchUI)
run_program.run()