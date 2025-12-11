from main.UI.homepage_UI import homepageUI
from main.UI.pickTimeOfTournament import PickTimeOfTournamentUI
from main.UI.teamLeaderBoardUI import TeamLeaderBoardUI
from main.UI.pickLeaderBoard import PickLeaderBoardUI
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


class MainUI():
    def __init__(self, homepage_ui: homepageUI, ptot_ui: PickTimeOfTournamentUI, pick_leader_board_ui: PickLeaderBoardUI, list_of_teams_ui: ListOfTeamsUI, list_of_clubs_ui: listOfClubsUI, login_ui: LoginUI, list_of_players_ui: ListOfPlayersUI, add_tournamnet_ui: AddTournamentUI, search_ui: SearchUI, team_ui: TeamUI, team_all_info_ui: TeamAllInfoUI, past_tournaments_list_ui: PastTournamentsUI, add_team_ui: AddTeamUI, team_leader_board_ui: TeamLeaderBoardUI):
        self.__homepage_ui = homepage_ui
        self.__ptot_ui = ptot_ui
        self.__pick_leader_board_ui = pick_leader_board_ui
        self.__list_of_teams_ui = list_of_teams_ui
        self.__list_of_clubs_ui = list_of_clubs_ui
        self.__login_ui = login_ui
        self.__list_of_players_ui = list_of_players_ui
        self.__add_tournament_ui = add_tournamnet_ui
        self.__search_ui = search_ui
        self.__team_ui = team_ui
        self.__team_all_info_ui = team_all_info_ui
        self.__past_tournaments_list_ui = past_tournaments_list_ui
        self.__add_team_ui = add_team_ui
        self.__team_leader_board_ui = team_leader_board_ui

        self.current_ui_page = "Homepage"
        self.isAdmin = False
        self.isATeamCapt = False
        self.nameOfTeamCaptTeamsName = ""
        self.nameOfATeam = ""
    
    # Here is the function to run the code
    def run(self):
        while True:
            # Check if you are on the homepage to set it to the correct page you choose
            if( self.current_ui_page == "Homepage"):
                # Here we get what page you wanted to go to
                action = self.__homepage_ui.print_menu(self, self.isAdmin, self.isATeamCapt)
                
                # Here we put set you to the page that lets you pick the time of the tournament
                if(action == "TIME"):
                    self.current_ui_page = "TIME_OF_TOURNAMENTS"
                
                # Here we put set you to the page that shows you the leader board for all teams and tournaments
                elif(action == "LEADER"):
                    self.current_ui_page = "PICK_LEADER_BOARD"
                
                # Here we put set you to the page that show you a list of all the teams
                elif(action == "TEAMS"):
                    self.current_ui_page = "LIST_OF_TEAMS"
                
                elif(action == "CLUBS"):
                    self.current_ui_page = "LIST_OF_CLUBS"

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
                
                # Here you're set to the page where you pick what you want to search for
                elif(action == "SEARCH"):
                    self.current_ui_page = "PICK_SEARCH"
                
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
                action = self.__ptot_ui.print_ptot_ui(self)
                
                # Here you're set to the page that holds all the old tournaments
                if(action == "Past"):
                    self.current_ui_page = "Past_Tournamnets"
                    
                # Here you're set to the page that holds all the tournaments that are still on going
                elif(action == "On going"):
                    self.current_ui_page = "On_Going_Tournaments"
                    print("not implamented")
                    break
                
                # Here you're set to the page that holds all the tournaments that in the future
                elif(action == "Future"):
                    self.current_ui_page = "Future_Tournaments"
                    print("not implamented")
                    break
                
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
            
            if(self.current_ui_page == "PICK_LEADER_BOARD"):
                action = self.__pick_leader_board_ui.print_plb_ui(self)
                if(action == "QUIT"):
                    break
                elif(action == "BACK"):
                    self.current_ui_page = "Homepage"
                elif(action == "TEAM"):
                    self.current_ui_page = "TEAM_LEADER_BOARD"

            if(self.current_ui_page == "TEAM_LEADER_BOARD"):
                action = self.__team_leader_board_ui.print_team_leader_board(self)
                if(action == "BACK"):
                    self.current_ui_page = "PICK_LEADER_BOARD"
                if(action == "QUIT"):
                    break

            if(self.current_ui_page == "LIST_OF_TEAMS"):
                action = self.__list_of_teams_ui.print_list_of_teams(self, self.isAdmin)
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
                pass
            
            if(self.current_ui_page == "LIST_OF_CLUBS"):
                print("not implamented")
                break

            if(self.current_ui_page == "LOG_IN"):
                action = self.__login_ui.print_login(self)
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
                action = self.__list_of_players_ui.print_list_of_players(self)
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
                    action = self.__team_all_info_ui.print_team_info(self, self.nameOfATeam, self.isAdmin, self.isATeamCapt)
                else:
                    action = self.__team_ui.print_team(self, self.nameOfATeam)
                if(action == "BACK"):
                    self.nameOfATeam = ""
                    self.current_ui_page = "LIST_OF_TEAMS"

                elif(action == "QUIT"):
                    break

            if(self.current_ui_page == "Past_Tournamnets"):
                action = self.__past_tournaments_list_ui.print_tournaments(self)
                break