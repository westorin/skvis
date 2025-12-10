from main.logic.leaderboardmanager import LeaderboardManager
from main.wrappers.datawrapper import DataWrapper
from main.logic.listOfPlayers import ListOfPlayersLogic
from main.logic.clearScreenInTerminal import clear_screen

data = DataWrapper()
leaderboard_manager = LeaderboardManager(data)

teams = leaderboard_manager.get_team_leaderboard()

page = leaderboard_manager.sort_leaderboard_into_a_list_of_tens()

current = 0

# print("=== Team Leaderboard ===")
# while True:
#     display_teams = page[current]
#     print(f"Page {current + 1} of {len(page)}")
#     for team in display_teams:
#         print(f"Place: {team['place']}, Team: {team['team']}, Matches: {team['matches']}, Wins: {team['wins']}, Losses: {team['losses']}, Winrate: {team['winrate']}%")
#     print("\n====")
#     print("d: Down Page | u: Up Page | q: Quit")

#     choice = input("Enter your choice: ").lower().strip()

#     if choice == "d":
#         if current < len(page) - 1:
#             current += 1
#         else:
#             print("You are already on the last page.")
#     elif choice == "u":
#         if current > 0:
#             current -= 1
#         else:
#             print("You are already on the first page.")
#     elif choice == "q":
#         break
#     else:
#         print("Invalid choice. Please enter 'd', 'u', or 'q'.")


# for team in teams:
#     print(f"Place: {team['place']}, Team: {team['team']}, Matches: {team['matches']}, Wins: {team['wins']}, Losses: {team['losses']}, Winrate: {team['winrate']}%")
# print(teams)
# print(teams[0]["team"])
# print(teams[0]["wins"])  # Example of accessing team name of the second team in the leaderboard


class ListOfTournamentUI():
    def __init__(self):
        pass

    def print_list_of_teams(self):
        self.list_of_players = LeaderboardManager().sort_leaderboard_into_a_list_of_tens()
        list_layer_counters = 1

    
        add_command = """|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     Enter the command you want or name of the player...     |\t\t\t\t\t\t\t\t|
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
            if(len(self.list_of_players) <= 1):
                up_down_command = """|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""

            elif(list_layer_counters == 1):
                up_down_command = """|\t\t\t\t\t\t\t|                  d. to go down the list                     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""

            elif(len(self.list_of_players) == list_layer_counters):
                up_down_command = """|\t\t\t\t\t\t\t|                   u. to go up the list                      |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""
                
            elif(len(self.list_of_players) > list_layer_counters and list_layer_counters > 1):
                up_down_command ="""|\t\t\t\t\t\t\t| u. to go up the list        | d. to go down the list        |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""

            header_text = f"""+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                                                   \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t     ╦  ┌─┐┌─┐┌┬┐┌─┐┬─┐┌┐ ┌─┐┌─┐┬─┐┌┬┐             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t     ║  ├┤ ├─┤ ││├┤ ├┬┘├┴┐│ │├─┤├┬┘ ││             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t     ╩═╝└─┘┴ ┴─┴┘└─┘┴└─└─┘└─┘┴ ┴┴└──┴┘             \t\t\t\t\t\t\t\t|    

\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                  \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | Place         | Team     | Matches.     | Wins     | Losses     | Winrate            |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +======================+======================+======================+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][0][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][0][0]))
                  } | {self.list_of_players[list_layer_counters-1][0][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][0][1]))
                       } | {self.list_of_players[list_layer_counters-1][0][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][0][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][1][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][1][0]))
                  } | {self.list_of_players[list_layer_counters-1][1][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][1][1]))
                       } | {self.list_of_players[list_layer_counters-1][1][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][1][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][2][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][2][0]))
                  } | {self.list_of_players[list_layer_counters-1][2][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][2][1]))
                       } | {self.list_of_players[list_layer_counters-1][2][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][2][2]))
                            } |\t\t\t\t\t\t\t|"""

            center_text = f"""|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][3][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][3][0]))
                  } | {self.list_of_players[list_layer_counters-1][3][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][3][1]))
                       } | {self.list_of_players[list_layer_counters-1][3][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][3][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][4][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][4][0]))
                  } | {self.list_of_players[list_layer_counters-1][4][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][4][1]))
                       } | {self.list_of_players[list_layer_counters-1][4][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][4][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][5][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][5][0]))
                  } | {self.list_of_players[list_layer_counters-1][5][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][5][1]))
                       } | {self.list_of_players[list_layer_counters-1][5][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][5][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][6][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][6][0]))
                  } | {self.list_of_players[list_layer_counters-1][6][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][6][1]))
                       } | {self.list_of_players[list_layer_counters-1][6][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][6][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|"""


            footer_text = f"""|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][7][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][7][0]))
                  } | {self.list_of_players[list_layer_counters-1][7][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][7][1]))
                       } | {self.list_of_players[list_layer_counters-1][7][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][7][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][8][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][8][0]))
                  } | {self.list_of_players[list_layer_counters-1][8][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][8][1]))
                       } | {self.list_of_players[list_layer_counters-1][8][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][8][2]))
                            } |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  +----------------------+----------------------+----------------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t  | {self.list_of_players[list_layer_counters-1][9][0] +" "*(20 -len(self.list_of_players[list_layer_counters-1][9][0]))
                  } | {self.list_of_players[list_layer_counters-1][9][1] +" "*(20 -len(self.list_of_players[list_layer_counters-1][9][1]))
                       } | {self.list_of_players[list_layer_counters-1][9][2] +" "*(20 -len(self.list_of_players[list_layer_counters-1][9][2]))
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