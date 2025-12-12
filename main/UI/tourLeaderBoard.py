from main.logic.clearScreenInTerminal import clear_screen

class TournamentLeaderBoardUI():
    def __init__(self, logic):
        self.logic = logic

    def print_leader_board(self, tournament_name: str):
        self.tournament_name = tournament_name

        leaderboard_manager = self.logic.leaderboard_manager

        page = leaderboard_manager.sort_leaderboard_into_a_list_of_tens()
        current_page = 1

        header_text = """+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\033[96m\033[1m+-------------------------------------+\033[0m\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\033[96m\033[1m|\033[0m ╦  ┌─┐┌─┐┌┬┐┌─┐┬─┐  ╔╗ ┌─┐┌─┐┬─┐┌┬┐ \033[96m\033[1m|\033[0m\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\033[96m\033[1m|\033[0m ║  ├┤ ├─┤ ││├┤ ├┬┘  ╠╩╗│ │├─┤├┬┘ ││ \033[96m\033[1m|\033[0m\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\033[96m\033[1m|\033[0m ╩═╝└─┘┴ ┴─┴┘└─┘┴└─  ╚═╝└─┘┴ ┴┴└──┴┘ \033[96m\033[1m|\033[0m\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\033[96m\033[1m+-------------------------------------+\033[0m\t\t\t\t\t\t\t\t\t|"""

        error_text ="""|\t\t\t\t\t\t+------------------------------------------------------------------------------+\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                              |\t\t\t\t\t\t|
|\t\t\t\t\t\t|     \x1b[33m^\x1b[0m                                                                        |\t\t\t\t\t\t|
|\t\t\t\t\t\t|    \x1b[33m/ \ \x1b[0m             You have entered an invalid input                        |\t\t\t\t\t\t|
|\t\t\t\t\t\t|   \x1b[33m/\x1b[0m \033[31m\033[1m|\033[0m \x1b[33m\ \x1b[0m                                                                     |\t\t\t\t\t\t|
|\t\t\t\t\t\t|  \x1b[33m/\x1b[0m  \033[31m\033[1m.\033[0m  \x1b[33m\  \x1b[0m            Enter Y. if you want to try again                      |\t\t\t\t\t\t|
|\t\t\t\t\t\t| \x1b[33m/_______\ \x1b[0m               or q. if you want to quit.                          |\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                              |\t\t\t\t\t\t|
|\t\t\t\t\t\t+------------------------------------------------------------------------------+\t\t\t\t\t\t|"""

        while True:

            top_leader_board_text = f"""|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m Nr.  \033[96m\033[1m|\033[0m Team name            \033[96m\033[1m|\033[0m Matches   \033[96m\033[1m|\033[0m wins      \033[96m\033[1m|\033[0m Losses    \033[96m\033[1m|\033[0m Win rate % \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+======+======================+===========+===========+===========+============+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][0]["place"] + " "*(4 -len(page[(current_page - 1)][0]["place"]))
                } \033[96m\033[1m|\033[0m {page[(current_page - 1)][0]["team"] + " "*(20 -len(page[(current_page - 1)][0]["team"]))
                     } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][0]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][0]["matches"])))
                          } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][0]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][0]["wins"])))
                               } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][0]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][0]["losses"])))
                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][0]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][0]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][1]["place"] + " "*(4 -len(page[(current_page - 1)][1]["place"]))
                } \033[96m\033[1m|\033[0m {page[(current_page - 1)][1]["team"] + " "*(20 -len(page[(current_page - 1)][1]["team"]))
                     } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][1]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][1]["matches"])))
                          } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][1]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][1]["wins"])))
                               } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][1]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][1]["losses"])))
                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][1]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][1]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|""" 
          
            center_leader_board_teaxt = f"""|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][2]["place"] + " "*(4 -len(page[(current_page - 1)][2]["place"]))
                                                               } \033[96m\033[1m|\033[0m {page[(current_page - 1)][2]["team"] + " "*(20 -len(page[(current_page - 1)][2]["team"]))
                                                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][2]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][2]["matches"])))
                                                                         } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][2]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][2]["wins"])))
                                                                              } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][2]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][2]["losses"])))
                                                                                   } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][2]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][2]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][3]["place"] + " "*(4 -len(page[(current_page - 1)][3]["place"]))
                } \033[96m\033[1m|\033[0m {page[(current_page - 1)][3]["team"] + " "*(20 -len(page[(current_page - 1)][3]["team"]))
                     } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][3]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][3]["matches"])))
                          } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][3]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][3]["wins"])))
                               } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][3]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][3]["losses"])))
                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][3]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][3]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][4]["place"] + " "*(4 -len(page[(current_page - 1)][4]["place"]))
                } \033[96m\033[1m|\033[0m {page[(current_page - 1)][4]["team"] + " "*(20 -len(page[(current_page - 1)][4]["team"]))
                     } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][4]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][4]["matches"])))
                          } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][4]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][4]["wins"])))
                               } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][4]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][4]["losses"])))
                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][4]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][4]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][5]["place"] + " "*(4 -len(page[(current_page - 1)][5]["place"]))
                } \033[96m\033[1m|\033[0m {page[(current_page - 1)][5]["team"] + " "*(20 -len(page[(current_page - 1)][5]["team"]))
                     } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][5]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][5]["matches"])))
                          } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][5]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][5]["wins"])))
                               } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][5]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][5]["losses"])))
                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][5]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][5]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][6]["place"] + " "*(4 -len(page[(current_page - 1)][6]["place"]))
                } \033[96m\033[1m|\033[0m {page[(current_page - 1)][6]["team"] + " "*(20 -len(page[(current_page - 1)][6]["team"]))
                     } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][6]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][6]["matches"])))
                          } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][6]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][6]["wins"])))
                               } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][6]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][6]["losses"])))
                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][6]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][6]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|""" 
               
            bottum_leader_board_text = f"""|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][7]["place"] + " "*(4 -len(page[(current_page - 1)][7]["place"]))
                } \033[96m\033[1m|\033[0m {page[(current_page - 1)][7]["team"] + " "*(20 -len(page[(current_page - 1)][7]["team"]))
                     } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][7]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][7]["matches"])))
                          } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][7]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][7]["wins"])))
                               } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][7]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][7]["losses"])))
                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][7]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][7]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][8]["place"] + " "*(4 -len(page[(current_page - 1)][8]["place"]))
                } \033[96m\033[1m|\033[0m {page[(current_page - 1)][8]["team"] + " "*(20 -len(page[(current_page - 1)][8]["team"]))
                     } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][8]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][8]["matches"])))
                          } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][8]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][8]["wins"])))
                               } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][8]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][8]["losses"])))
                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][8]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][8]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m|\033[0m {page[(current_page - 1)][9]["place"] + " "*(4 -len(page[(current_page - 1)][9]["place"]))
                } \033[96m\033[1m|\033[0m {page[(current_page - 1)][9]["team"] + " "*(20 -len(page[(current_page - 1)][9]["team"]))
                     } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][9]["matches"]) + " "*(9 -len(str(page[(current_page - 1)][9]["matches"])))
                          } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][9]["wins"]) + " "*(9 -len(str(page[(current_page - 1)][9]["wins"])))
                               } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][9]["losses"]) + " "*(9 -len(str(page[(current_page - 1)][9]["losses"])))
                                    } \033[96m\033[1m|\033[0m {str(page[(current_page - 1)][9]["winrate"]) + " "*(10 -len(str(page[(current_page - 1)][9]["winrate"])))} \033[96m\033[1m|\033[0m\t\t\t\t\t\t|
|\t\t\t\t\t\t\033[96m\033[1m+------+----------------------+-----------+-----------+-----------+------------+\033[0m\t\t\t\t\t\t|"""

            if(len(page) <= 1):
                up_down_command = """|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m b. To go back               \033[30m\033[1m|\033[0m q. To quit  the program       \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""

            elif(current_page == 1):
                up_down_command = """|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m                  d. to go down the list                     \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m b. To go back               \033[30m\033[1m|\033[0m q. To quit  the program       \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|"""

            elif(len(page) == current_page):
                up_down_command = """|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m                   u. to go up the list                      \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m b. To go back               \033[30m\033[1m|\033[0m q. To quit  the program       \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|"""
                
            elif(len(page) > current_page and current_page > 1):
                up_down_command ="""|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m u. to go up the list        \033[30m\033[1m|\033[0m d. to go down the list        \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m b. To go back               \033[30m\033[1m|\033[0m q. To quit  the program       \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-----------------------------+-------------------------------+\033[0m\t\t\t\t\t\t\t\t|"""

            footer_text = f"""|\t\t\t\t\t\t\t\033[30m\033[1m+-------------------------------------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m                  Enter command you want...                  |\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+=============================================================+\033[0m\t\t\t\t\t\t\t\t|
{up_down_command}
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""

            clear_screen()
            print(header_text)
            print(top_leader_board_text)
            print(center_leader_board_teaxt)
            print(bottum_leader_board_text)
            print(footer_text)
            choice = str(input(">>>> "))
               
               
            if(choice.lower() == "u" and 1 < current_page):
                current_page -= 1
            elif(choice.lower() == "d" and len(page) > current_page):
                current_page += 1
            elif(choice.lower() == "b"):
                return "BACK"
            elif(choice.lower() == "q"):
                return "QUIT"
            else:
                clear_screen()
                print(header_text)
                print(top_leader_board_text)
                print(error_text)
                print(bottum_leader_board_text)
                print(footer_text)

                choice = str(input(">>>> "))

                if(choice.lower() == "q"):
                    return "BACK"
