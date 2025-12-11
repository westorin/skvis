from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

from main.logic.listOfTeams import ListOfTeamsLogic #<-- This needs to go
from main.logic.clearScreenInTerminal import clear_screen

class ListOfTeamsUI():
    def __init__(self):
        data = DataWrapper()
        logic = LogicWrapper(data)
        self.tm = logic.team_manager

    def print_list_of_teams(self, isAdminFromMain: bool) -> str:
        self.isAdmin = isAdminFromMain
        self.list_of_teams = ListOfTeamsLogic().sort_teams_into_a_list_of_tens()
        self.list_of_teams = self.tm.sort_teams_into_a_list_of_tens() #<-- This needs to go. Can replace it with the code above
        list_layer_counters = 1

        data = DataWrapper()
        logic = LogicWrapper(data)
        tm = logic.team_manager

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

        error_text ="""|\t\t\t\t\t\t+------------------------------------------------------------------------+  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                        |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|     ^                                                                  |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|    / \             You have entered an invalid input                   |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|   / | \                                                                |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|  /  .  \            Enter Y. if you want to try again                  |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t| /_______\               or q. if you want to quit.                     |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                        |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t+------------------------------------------------------------------------+  \t\t\t\t\t\t\t|"""
        
        while True:
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

            header_text = f"""+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            +-------------------------------------+            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            | ╦  ┬┌─┐┌┬┐  ┌─┐┌─┐  ┌┬┐┌─┐┌─┐┌┬┐┌─┐ |            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            | ║  │└─┐ │   │ │├┤    │ ├┤ ├─┤│││└─┐ |            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            | ╩═╝┴└─┘ ┴   └─┘└     ┴ └─┘┴ ┴┴ ┴└─┘ |            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t            +-------------------------------------+            \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | Team name            | Team Capt.           | URL                  |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +======================+======================+======================+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][0][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][0][0]))
                  } | {self.list_of_teams[list_layer_counters-1][0][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][0][1]))
                       } | {self.list_of_teams[list_layer_counters-1][0][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][0][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][1][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][1][0]))
                  } | {self.list_of_teams[list_layer_counters-1][1][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][1][1]))
                       } | {self.list_of_teams[list_layer_counters-1][1][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][1][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][2][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][2][0]))
                  } | {self.list_of_teams[list_layer_counters-1][2][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][2][1]))
                       } | {self.list_of_teams[list_layer_counters-1][2][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][2][2]))
                            } |\t\t\t\t\t\t\t|"""

            center_text = f"""|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][3][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][3][0]))
                  } | {self.list_of_teams[list_layer_counters-1][3][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][3][1]))
                       } | {self.list_of_teams[list_layer_counters-1][3][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][3][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][4][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][4][0]))
                  } | {self.list_of_teams[list_layer_counters-1][4][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][4][1]))
                       } | {self.list_of_teams[list_layer_counters-1][4][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][4][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][5][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][5][0]))
                  } | {self.list_of_teams[list_layer_counters-1][5][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][5][1]))
                       } | {self.list_of_teams[list_layer_counters-1][5][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][5][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][6][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][6][0]))
                  } | {self.list_of_teams[list_layer_counters-1][6][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][6][1]))
                       } | {self.list_of_teams[list_layer_counters-1][6][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][6][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|"""


            footer_text = f"""|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][7][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][7][0]))
                  } | {self.list_of_teams[list_layer_counters-1][7][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][7][1]))
                       } | {self.list_of_teams[list_layer_counters-1][7][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][7][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][8][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][8][0]))
                  } | {self.list_of_teams[list_layer_counters-1][8][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][8][1]))
                       } | {self.list_of_teams[list_layer_counters-1][8][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][8][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_teams[list_layer_counters-1][9][0] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][9][0]))
                  } | {self.list_of_teams[list_layer_counters-1][9][1] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][9][1]))
                       } | {self.list_of_teams[list_layer_counters-1][9][2] +" "*(20 -len(self.list_of_teams[list_layer_counters-1][9][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
{add_command}
{up_down_command}
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""
        
            clear_screen()

            print(header_text)
            print(center_text)
            print(footer_text)    
            
            choice = str(input(">>>>"))
            
            if(choice.lower() == "u" and 1 < list_layer_counters):
                list_layer_counters -= 1
            elif(choice.lower() == "d" and len(self.list_of_teams) > list_layer_counters):
                list_layer_counters += 1
            elif(choice.lower() == "b"):
                return "BACK"
            elif(choice.lower() == "q"):
                return "QUIT"
            elif(choice.lower() == "a" and self.isAdmin == True):
                return "ADD_TE"
            #elif(self.tm.does_team_exist(choice.lower()) == True): 
            elif(tm.does_team_exist(choice.lower()) == True): # <-- This needs to go. Can replace it with the code above
                return "TEAM", choice

            else:
                clear_screen()

                print(header_text)
                print(error_text)
                print(footer_text)

                choice = str(input(">>>>"))

                if(choice.lower() == "q"):
                    return "BACK"

                
            