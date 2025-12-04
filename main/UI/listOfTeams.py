from main.logic.listOfTeams import ListOfTeamsLogic
from main.logic.clearScreenInTerminal import clear_screen

class ListOfTeamsUI():
    def __init__(self):
        self.list_of_teams = ListOfTeamsLogic().sort_teams_into_a_list_of_tens()

#        teams = ListOfTeamsLogic().get_all_teams()
 #       logic = ListOfTeamsLogic()
        
    def print_list_of_teams(self, isAdminFromMain: bool) -> str:
        self.isAdmin = isAdminFromMain
        list_layer_counters = 1

        if(self.isAdmin == True):
            add_command = """|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|      Enter the command you want or name of the team...      |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                     a. Add a new team                       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""

        else:
            add_command = """|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|      Enter the command you want or name of the team...      |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+=============================+===============================+\t\t\t\t\t\t\t\t|"""

        error_text ="""|\t\t\t\t\t\t  +--------------------------------------------------------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |                                                                    |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |     ^                                                              |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |    / \              You have entered an invalid input              |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |   / | \                                                            |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |  /  .  \            Enter Y. if you want to try again              |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | /_______\               or q. if you want to quit.                 |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |                                                                    |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +--------------------------------------------------------------------+\t\t\t\t\t\t\t|"""

        if(len(self.list_of_teams) <= 1):
            up_down_command = """|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""

        elif(list_layer_counters == 1):
            up_down_command = """|\t\t\t\t\t\t\t|                  d. to go down the list                     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""

        elif(len(self.list_of_teams) == list_layer_counters):
            up_down_command = """|\t\t\t\t\t\t\t|                   u. to go up the list                      |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""
        
        elif(len(self.list_of_teams) > list_layer_counters and list_layer_counters > 1):
            up_down_command ="""|\t\t\t\t\t\t\t| u. to go up the list        | d. to go down the list        |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""

        header = f"""+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            +-------------------------------------+            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            | ╦  ┬┌─┐┌┬┐  ┌─┐┌─┐  ┌┬┐┌─┐┌─┐┌┬┐┌─┐ |            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            | ║  │└─┐ │   │ │├┤    │ ├┤ ├─┤│││└─┐ |            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            | ╩═╝┴└─┘ ┴   └─┘└     ┴ └─┘┴ ┴┴ ┴└─┘ |            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            +-------------------------------------+            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | Team name            | Team Capt.           | URL                  |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +======================+======================+======================+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|"""

        center_text = f"""|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|"""

        error_text ="""|\t\t\t\t\t\t  +--------------------------------------------------------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |                                                                    |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |     ^                                                              |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |    / \              You have entered an invalid input              |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |   / | \                                                            |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |  /  .  \            Enter Y. if you want to try again              |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | /_______\               or q. if you want to quit.                 |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  |                                                                    |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +--------------------------------------------------------------------+\t\t\t\t\t\t\t|"""        

        footer_text = f"""|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {" "*20} | {" "*20} | {" "*20} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
{add_command}
{up_down_command}
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""
    
    
        clear_screen()
        print(header)
        print(center_text)
        print(footer_text)
    