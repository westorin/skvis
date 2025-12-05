from main.UI.homepage_UI import homepageUI
from main.UI.pickTimeOfTournament import PickTimeOfTournamntsUI
from main.UI.leaderboard import LeaderBoardUI
from main.UI.listOfTeams import ListOfTeamsUI
from main.UI.listOfClubs import listOfClubsUI
from main.UI.login import LoginUI
from main.UI.listOfPlayers import ListOfPlayersUI
from main.UI.addtournament import AddTournamentUI
from main.UI.search import SearchUI

class MainUI():
    def __init__(self, homepage_ui: homepageUI, ptot_ui: PickTimeOfTournamntsUI, leader_board_ui: LeaderBoardUI, list_of_teams_ui: ListOfTeamsUI, list_of_clubs_ui: listOfClubsUI, login_ui: LoginUI, list_of_players_ui: ListOfPlayersUI, add_tournamnet_ui: AddTournamentUI, search_ui: SearchUI):
        self.__homepage_ui = homepage_ui
        self.__ptot_ui = ptot_ui
        self.__leader_board_ui = leader_board_ui
        self.__list_of_teams_ui = list_of_teams_ui
        self.__list_of_clubs_ui = list_of_clubs_ui
        self.__login_ui = login_ui
        self.__list_of_players_ui = list_of_players_ui
        self.__add_tournament_ui = add_tournamnet_ui
        self.__search_ui = search_ui

        self.current_ui_page = "Homepage"
        self.isAdmin = False
        self.isATeamCapt = False
    
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
                    self.current_ui_page = "LEADER_BOARD"
                
                # Here we put set you to the page that show you a list of all the teams
                elif(action == "TEAMS"):
                    self.current_ui_page = "LIST_OF_TEAMS"
                
                elif(action == "CLUBS"):
                    self.current_ui_page = "LIST_OF_CLUBS"

                # Here you are sign out of being an admin or a team captian if you are loged in
                elif(action == "SIGN"):
                    self.isAdmin = False
                    self.isATeamCapt = False
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
                    print("not implamented")
                    break
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
            
            if(self.current_ui_page == "LEADER_BOARD"):
                print("not implamented")
                break

            if(self.current_ui_page == "LIST_OF_TEAMS"):
                action = self.__list_of_teams_ui.print_list_of_teams(self, self.isAdmin)
                if(action == "BACK"):
                    self.current_ui_page = "Homepage"
                elif(action == "QUIT"):
                    break
                elif(action == "ADD_TE"):
                    self.current_ui_page = "ADD_TEAM"
                    print("NOT IMPLAMENTED!!!!!!!!!!!!!!!")
                    break
            
            if(self.current_ui_page == "LIST_OF_CLUBS"):
                print("not implamented")
                break

            if(self.current_ui_page == "LOG_IN"):
                # role = self.__login_ui.print_login_ui(self)

                # if role:
                #     self.isAdmin = False
                #     self.isATeamCapt = False

                #     if role == "admin":
                #         self.isAdmin = True
                #     elif role == "captain":
                #         self.isATeamCapt = True

                #     print(f"Logged in as {role}")
                # else:
                #     print("Login failed. Please try again.")

                # self.current_ui_page = "Homepage"
                # continue
                print("not implamented")
                break

            if(self.current_ui_page == "LIST_OF_PLAYERS"):
                print("not implamented")
                break

            if(self.current_ui_page == "ADD_TOURNAMENT"):
                print("not implamented")
                break

            if(self.current_ui_page == "PICK_SEARCH"):
                print("not implamented")
                break