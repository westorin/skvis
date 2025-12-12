from main.logic.listOfPlayers import ListOfPlayersLogic
from main.logic.clearScreenInTerminal import clear_screen


class ListOfPlayersUI():
    def __init__(self):
        pass

    def print_list_of_players(self):
        self.list_of_players = ListOfPlayersLogic().sort_players_into_pers_of_ten()
        list_layer_counters = 1

    
        add_command = """|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-------------------------------------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m     Enter the command you want or name of the player...     \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+=============================+===============================+\033[0m\t\t\t\t\t\t\t\t|"""

        error_text ="""|\t\t\t\t\t\t+------------------------------------------------------------------------+  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                        |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|     \x1b[33m^\x1b[0m                                                                  |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|    \x1b[33m/ \ \x1b[0m             You have entered an invalid input                  |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|   \x1b[33m/\x1b[0m \033[31m\033[1m|\033[0m \x1b[33m\ \x1b[0m                                                               |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|  \x1b[33m/\x1b[0m  \033[31m\033[1m.\033[0m  \x1b[33m\  \x1b[0m            Enter Y. if you want to try again                |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t| \x1b[33m/_______\ \x1b[0m               or q. if you want to quit.                    |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                        |  \t\t\t\t\t\t\t|
|\t\t\t\t\t\t+------------------------------------------------------------------------+  \t\t\t\t\t\t\t|"""
        
        while True:
            if(len(self.list_of_players) <= 1):
                up_down_command = """|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m b. To go back               \033[30m\033[1m|\033[0m q. To quit  the program       \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""

            elif(list_layer_counters == 1):
                up_down_command = """|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m                  d. to go down the list                     \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m b. To go back               \033[30m\033[1m|\033[0m q. To quit  the program       \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|"""

            elif(len(self.list_of_players) == list_layer_counters):
                up_down_command = """|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m                   u. to go up the list                      \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m b. To go back               \033[30m\033[1m|\033[0m q. To quit  the program       \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|"""
                
            elif(len(self.list_of_players) > list_layer_counters and list_layer_counters > 1):
                up_down_command ="""|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m u. to go up the list        \033[30m\033[1m|\033[0m d. to go down the list        \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m b. To go back               \033[30m\033[1m|\033[0m q. To quit  the program       \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|"""

            header_text = f"""+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         \033[34m\033[1m+-------------------------------------------+\033[0m         \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         \033[34m\033[1m|\033[0m ╦  ┬┌─┐┌┬┐  ┌─┐┌─┐  ┌─┐┬  ┌─┐┬ ┬┌─┐┬─┐┌─┐ \033[34m\033[1m|\033[0m         \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         \033[34m\033[1m|\033[0m ║  │└─┐ │   │ │├┤   ├─┘│  ├─┤└┬┘├┤ ├┬┘└─┐ \033[34m\033[1m|\033[0m         \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         \033[34m\033[1m|\033[0m ╩═╝┴└─┘ ┴   └─┘└    ┴  ┴─┘┴ ┴ ┴ └─┘┴└─└─┘ \033[34m\033[1m|\033[0m         \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         \033[34m\033[1m+-------------------------------------------+\033[0m         \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m Players name         \033[34m\033[1m|\033[0m Players username     \033[34m\033[1m|\033[0m Team                 \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+======================+======================+======================+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][0][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][0][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][0][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][0][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][0][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][0][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][1][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][1][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][1][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][1][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][1][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][1][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][2][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][2][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][2][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][2][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][2][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][2][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|"""

            center_text = f"""|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][3][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][3][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][3][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][3][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][3][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][3][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][4][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][4][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][4][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][4][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][4][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][4][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][5][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][5][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][5][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][5][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][5][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][5][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][6][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][6][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][6][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][6][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][6][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][6][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|"""


            footer_text = f"""|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][7][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][7][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][7][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][7][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][7][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][7][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][8][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][8][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][8][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][8][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][8][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][8][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][9][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][9][0]))
                  } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][9][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][9][1]))
                       } \033[34m\033[1m|\033[0m {self.list_of_players[list_layer_counters-1][9][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][9][2]))
                            } \033[34m\033[1m|\033[0m\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  \033[34m\033[1m+----------------------+----------------------+----------------------+\033[0m\t\t\t\t\t\t\t|
{add_command}
{up_down_command}
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""
        
            clear_screen()

            print(header_text)
            print(center_text)
            print(footer_text)   
            
            choice = str(input(">>>> "))
            
            if(choice.lower() == "u" and 1 < list_layer_counters):
                list_layer_counters -= 1
            elif(choice.lower() == "d" and len(self.list_of_players) > list_layer_counters):
                list_layer_counters += 1
            elif(choice.lower() == "b"):
                return "BACK"
            elif(choice.lower() == "q"):
                return "QUIT"
            # TODO Need to add show a player
            else:
                clear_screen()

                print(header_text)
                print(error_text)
                print(footer_text)

                choice = str(input(">>>>"))

                if(choice.lower() == "q"):
                    return "BACK"