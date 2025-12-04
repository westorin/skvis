'''
To run the main UI type this into terminal: 

python3 -m main.UI.mainUI
or
python3 run.py

'''
from main.UI.createplayerUI import PlayerUI
from main.logic.clearScreenInTerminal import clear_screen
from main.UI.homepage_UI import homepageUI
from main.UI.pickTimeOfTournament import PickTimeOfTournamntsUI

class MainUI():
    def __init__(self, homepage_UI: homepageUI, ptot_ui: PickTimeOfTournamntsUI):
        self.__homepage_UI = homepageUI
        self.__ptot_ui = PickTimeOfTournamntsUI
        self.current_ui_page = "Homepage"
    
    def run(self):
        while True:
            if( self.current_ui_page == "Homepage"):
                action = self.__homepage_UI.print_menu(self)
                if(action == "TIME"):
                    self.current_ui_page = "TIME_OF_TOURNAMENTS"
                if(action == "QUIT"):
                    self.current_ui_page = "Quit"
                    break

            if(self.current_ui_page == "TIME_OF_TOURNAMENTS"):
                action = self.__ptot_ui.print_ptot_ui(self)
                if(action == "Past"):
                    self.current_ui_page = "Past_Tournamnets"
                elif(action == "On going"):
                    self.current_ui_page = "On_Going_Tournaments"
                elif(action == "Future"):
                    self.current_ui_page = "Future_Tournaments"
                elif(action == "BACK"):
                    self.current_ui_page = "Homepage"
                elif(action == "QUIT"):
                    self.current_ui_page = "Quit"
                    break
                else:
                    print("Error in main UI. not sent to the currect UI page in Ptot")
                    break



#if __name__ == "__main__":
    #main()