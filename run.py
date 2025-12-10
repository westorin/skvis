from main.UI.mainUI import MainUI
from main.UI.homepage_UI import homepageUI 
from main.UI.pickTimeOfTournament import PickTimeOfTournamentUI
from main.UI.leaderboardUI import LeaderBoardUI
from main.UI.listOfTeams import ListOfTeamsUI
from main.UI.listOfClubs import listOfClubsUI
from main.UI.login import LoginUI
from main.UI.listOfPlayers import ListOfPlayersUI
from main.UI.addtournament import AddTournamentUI
from main.UI.search import SearchUI
from main.UI.team import TeamUI
from main.UI.teamAllInfo import TeamAllInfoUI



run_program = MainUI(homepageUI, PickTimeOfTournamentUI, LeaderBoardUI, ListOfTeamsUI, listOfClubsUI, LoginUI, ListOfPlayersUI, AddTournamentUI, SearchUI, TeamUI, TeamAllInfoUI)
run_program.run()
