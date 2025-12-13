from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

from main.UI.homepage_UI import homepageUI
from main.UI.pickTimeOfTournament import PickTimeOfTournamentUI
from main.UI.teamLeaderBoardUI import TeamLeaderBoardUI
from main.UI.listOfTeams import ListOfTeamsUI
from main.UI.login import LoginUI
from main.UI.listOfPlayers import ListOfPlayersUI
from main.UI.addtournament import AddTournamentUI
from main.UI.team import TeamUI
from main.UI.teamAllInfo import TeamAllInfoUI
from main.UI.pastTournamentsList import PastTournamentsUI
from main.UI.addTeam import AddTeamUI
from main.UI.onGoingTournamentsList import OnGoingTournamentsUI
from main.UI.futureTournamentsList import FutureTournamentsUI
from main.UI.tournamentInfo import TournamentInfoUI
from main.UI.schedule import ScheduleUI
from main.UI.tourLeaderBoard import TournamentLeaderBoardUI
from main.UI.tournamentMatch import TournamentMatchsUI
#from main.UI.TournamentUI import TournamentUI

class MainUI():
    def __init__(self):
        self.__homepage_ui = homepageUI(LogicWrapper(DataWrapper()))
        self.__ptot_ui = PickTimeOfTournamentUI(LogicWrapper(DataWrapper()))
        self.__list_of_teams_ui = ListOfTeamsUI(LogicWrapper(DataWrapper()))
        self.__login_ui = LoginUI(LogicWrapper(DataWrapper()))
        self.__list_of_players_ui = ListOfPlayersUI(LogicWrapper(DataWrapper()))
        self.__add_tournament_ui = AddTournamentUI(LogicWrapper(DataWrapper()))
        self.__team_ui = TeamUI(LogicWrapper(DataWrapper()))
        self.__team_all_info_ui = TeamAllInfoUI(LogicWrapper(DataWrapper()))
        self.__past_tournaments_list_ui = PastTournamentsUI(LogicWrapper(DataWrapper()))
        self.__add_team_ui = AddTeamUI(LogicWrapper(DataWrapper()))
        self.__team_leader_board_ui = TeamLeaderBoardUI(LogicWrapper(DataWrapper()))
        self.__on_going_tournaments_ui = OnGoingTournamentsUI(LogicWrapper(DataWrapper()))
        self.__future_tournaments_ui = FutureTournamentsUI(LogicWrapper(DataWrapper()))
        self.__tournament_info_ui = TournamentInfoUI(LogicWrapper(DataWrapper()))
        self.__schedule_ui = ScheduleUI(LogicWrapper(DataWrapper()))
        self.__tour_leader_ui = TournamentLeaderBoardUI(LogicWrapper(DataWrapper()))
        self.__tournament_matchs_ui = TournamentMatchsUI(LogicWrapper(DataWrapper()))
        self.__input_match_results_ui = TournamentUI(LogicWrapper(DataWrapper()))

        self.current_ui_page = "Homepage"
        self.isAdmin = False
        self.isATeamCapt = False
        self.nameOfTeamCaptTeamsName = ""
        self.nameOfATeam = ""
        self.nameOfATournament = ""
    
    # Here is the function to run the code
    def run(self):
        while True:
            # Check if you are on the homepage to set it to the correct page you choose
            if( self.current_ui_page == "Homepage"):
                # Here we get what page you wanted to go to
                action = self.__homepage_ui.print_menu(self.isAdmin, self.isATeamCapt)
                
                # Here we put set you to the page that lets you pick the time of the tournament
                if(action == "TIME"):
                    self.current_ui_page = "TIME_OF_TOURNAMENTS"
                
                # Here we put set you to the page that shows you the leader board for all teams and tournaments
                elif(action == "LEADER"):
                    self.current_ui_page = "LEADER_BOARD"
                
                # Here we put set you to the page that show you a list of all the teams
                elif(action == "TEAMS"):
                    self.current_ui_page = "LIST_OF_TEAMS"

                # Here you are sign out of being an admin or a team captian if you are loged in
                elif(action == "SIGN"):
                    self.isAdmin = False
                    self.isATeamCapt = False
                    self.captName = ""
                    self.current_ui_page = "Homepage"
                
                # Here we set you to the page that lets you log in
                elif(action == "LOGIN"):
                    self.current_ui_page = "LOG_IN"
                
                # Here you are set to the page that shows you a list of all the players saved
                elif(action == "PLAYERS"):
                    self.current_ui_page = "LIST_OF_PLAYERS"
                
                # Here you're set to the page that allows you to add tournament if and only if you are loged in
                elif(action == "ADD"):
                    self.current_ui_page = "ADD_TOURNAMENT"
                
                # Here we end the program
                elif(action == "QUIT"):
                    self.current_ui_page = "Quit"
                    break
                
                else:
                    print("Error in main UI. not sent to the currect UI page in Homepage")
                    break
            
            # Check if you are on the Pick the time of the tournaments to set it to the correct page you choose
            if(self.current_ui_page == "TIME_OF_TOURNAMENTS"):

                # Here we get where you want to go next
                action = self.__ptot_ui.print_ptot_ui()
                
                # Here you're set to the page that holds all the old tournaments
                if(action == "PAST"):
                    self.current_ui_page = "PAST_TOURNAMENTS"
                    
                # Here you're set to the page that holds all the tournaments that are still on going
                elif(action == "ON_GOING"):
                    self.current_ui_page = "ON_GOING_TOURNAMENTS"
                
                # Here you're set to the page that holds all the tournaments that in the future
                elif(action == "FUTURE"):
                    self.current_ui_page = "FUTURE_TOURNAMENTS"
                
                # Here you're set to the page you where just on
                elif(action == "BACK"):
                    self.current_ui_page = "Homepage"
                
                # Here we end the program
                elif(action == "QUIT"):
                    self.current_ui_page = "Quit"
                    break
                
                else:
                    print("Error in main UI. not sent to the currect UI page in Ptot")
                    break

            if(self.current_ui_page == "LEADER_BOARD"):
                action = self.__team_leader_board_ui.print_team_leader_board()
                
                if(action == "BACK"):
                    self.current_ui_page = "Homepage"
                
                if(action == "QUIT"):
                    break

            if(self.current_ui_page == "LIST_OF_TEAMS"):
                action = self.__list_of_teams_ui.print_list_of_teams(self.isAdmin)
                
                if(action == "BACK"):
                    self.current_ui_page = "Homepage"
                
                elif(action == "QUIT"):
                    break
                
                elif(action == "ADD_TE"):
                    self.current_ui_page = "ADD_TEAM"
                
                elif(action[0] == "TEAM"):
                    self.current_ui_page = "A_TEAM"
                    self.nameOfATeam = action[1]

            if(self.current_ui_page == "ADD_TEAM"):
                action = self.__add_team_ui.print_add_team()
                
                if(action == "QUIT"):
                    break
                
                elif(action == "BACK"):
                    self.current_ui_page = "LIST_OF_TEAMS"

            
            if(self.current_ui_page == "LIST_OF_CLUBS"):
                print("not implamented")
                break

            if(self.current_ui_page == "LOG_IN"):
                action = self.__login_ui.print_login()
                
                if(action == "BACK"):
                    self.current_ui_page = "Homepage"
                
                elif(action == "QUIT"):
                    break
                
                elif(action == "ADMIN"):
                    self.current_ui_page ="Homepage"
                    self.isAdmin = True
                
                elif(action[0] == "CAPT"):
                    self.current_ui_page = "Homepage"
                    self.isATeamCapt = True
                    self.nameOfTeamCaptTeamsName = action[1]

            if(self.current_ui_page == "LIST_OF_PLAYERS"):
                action = self.__list_of_players_ui.print_list_of_players()
                
                if(action == "BACK"):
                    self.current_ui_page = "Homepage"
                
                elif(action == "QUIT"):
                    break

            if(self.current_ui_page == "ADD_TOURNAMENT"):
                print("not implamented")
                break

            if(self.current_ui_page == "PICK_SEARCH"):
                print("not implamented")
                break

            if(self.current_ui_page == "A_TEAM"):
                if((self.nameOfTeamCaptTeamsName.lower() == self.nameOfATeam.lower() and self.isATeamCapt == True) or self.isAdmin == True):
                    action = self.__team_all_info_ui.print_team_info(self.nameOfATeam, self.isAdmin, self.isATeamCapt)
                
                else:
                    action = self.__team_ui.print_team(self.nameOfATeam)
                
                if(action == "BACK"):
                    self.nameOfATeam = ""
                    self.current_ui_page = "LIST_OF_TEAMS"

                elif(action == "QUIT"):
                    break

            if(self.current_ui_page == "PAST_TOURNAMENTS"):
                action = self.__past_tournaments_list_ui.print_tournaments()
                
                if(action == "QUIT"):
                    break
                
                elif(action == "BACK"):
                    self.current_ui_page = "TIME_OF_TOURNAMENTS"
                
                elif(action[0] == "TOUR_INFO"):
                    self.nameOfATournament = action[1]
                    self.current_ui_page = "TOURNAMENT_INFO"

            if(self.current_ui_page == "ON_GOING_TOURNAMENTS"):
                action = self.__on_going_tournaments_ui.print_tournaments()
                
                if(action == "QUIT"):
                    break
                
                elif(action == "BACK"):
                    self.current_ui_page = "TIME_OF_TOURNAMENTS"
                
                elif(action[0] == "TOUR_INFO"):
                    self.nameOfATournament = action[1]
                    self.current_ui_page = "TOURNAMENT_INFO"

            if(self.current_ui_page == "FUTURE_TOURNAMENTS"):
                action = self.__future_tournaments_ui.print_tournaments()
                
                if(action == "QUIT"):
                    break
                
                elif(action == "BACK"):
                    self.current_ui_page = "TIME_OF_TOURNAMENTS"
                
                elif(action[0] == "TOUR_INFO"):
                    self.nameOfATournament = action[1]
                    self.current_ui_page = "TOURNAMENT_INFO"

            if(self.current_ui_page == "TOURNAMENT_INFO"):
                action = self.__tournament_info_ui.print_info(self.nameOfATournament, self.isAdmin)
                
                if(action == "QUIT"):
                    break
                
                elif(action == "BACK"):
                    self.current_ui_page = "TIME_OF_TOURNAMENTS"
                    self.nameOfATournament = ""
                
                elif(action == "SCHEDULE"):
                    self.current_ui_page = "TOURNAMENT_SCHEDULE"
                
                elif(action == "TOUR_LEADER"):
                    self.current_ui_page = "TOURNAMENT_LEADER_BOARD"

                elif(action == "GAME_BY_GAME"):
                    self.current_ui_page = "TOURNAMENT_MATCHS"

                elif(action == "UPDATE_MATCH"):
                    self.current_ui_page = "INPUT_MATCH_RESULTS"

            if(self.current_ui_page == "TOURNAMENT_SCHEDULE"):
                action = self.__schedule_ui.print_schedule(self.nameOfATournament)
                
                if(action == "QUIT"):
                    break
                
                elif(action == "BACK"):
                    self.current_ui_page = "TOURNAMENT_INFO"
            
            if(self.current_ui_page == "TOURNAMENT_LEADER_BOARD"):
                action = self.__tour_leader_ui.print_leader_board(self.nameOfATournament)

                if(action == "QUIT"):
                    break
                
                elif(action == "BACK"):
                    self.current_ui_page = "TOURNAMENT_INFO"

            if(self.current_ui_page == "TOURNAMENT_MATCHS"):
                action = self.__tournament_matchs_ui.print_matchs(self.nameOfATournament)
                if(action == "QUIT"):
                    break

                elif(action == "BACK"):
                    self.current_ui_page = "TOURNAMENT_INFO"

            if(self.current_ui_page == "ADD_TOURNAMENT"):
                action = self.__add_tournament_ui.add_tournament_ui()
                if(action == "BACK"):
                    self.current_ui_page = "Homepage"

            if(self.current_ui_page == "INPUT_MATCH_RESULTS"):
                action = self.__input_match_results_ui.run_tournament_ui()
