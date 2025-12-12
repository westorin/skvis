from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper
from main.logic.clearScreenInTerminal import clear_screen
import math

class ScheduleUI():
    def print_schedule(self, tournament_name):
        data = DataWrapper()
        logic = LogicWrapper(data)


        tour_data = data.tournaments.get_by_name(tournament_name)
        schedule_pages = logic.tournament_manager.get_schedule_pages(tournament_name)

        current_page = 1

        error_text ="""|\t\t\t\t+---------------------------------------------------------------------------------------------------------------+\t\t\t\t|
|\t\t\t\t|                                                                                                               |\t\t\t\t|
|\t\t\t\t|        ^                                                                                                      |\t\t\t\t|
|\t\t\t\t|       / \                         You have entered an invalid input                                           |\t\t\t\t|
|\t\t\t\t|      / | \                                                                                                    |\t\t\t\t|
|\t\t\t\t|     /  .  \                       Enter Y. if you want to try again                                           |\t\t\t\t|
|\t\t\t\t|    /_______\                         or q. if you want to quit.                                               |\t\t\t\t|
|\t\t\t\t|                                                                                                               |\t\t\t\t|
|\t\t\t\t+---------------------------------------------------------------------------------------------------------------+\t\t\t\t|"""

        header_text = f"""+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         +------------------------------------------+          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         | {" "*math.floor((40 -len(tour_data.name)) /2) + tour_data.name + " "*math.ceil((40 -len(tour_data.name)) /2)} |          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         +------------------------------------------+          \t\t\t\t\t\t\t\t|""" 

        while True:
            top_list_text = f"""|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t| Game nr. | Team A               |     | Team B               | Date       | Start time | Location             |\t\t\t\t|
|\t\t\t\t+==========+======================+=====+======================+============+============+======================+\t\t\t\t|
|\t\t\t\t| {schedule_pages[current_page - 1][0][0] + " "*(8 -len(schedule_pages[current_page - 1][0][0]))
            } | {schedule_pages[current_page - 1][0][1] + " "*(20 -len(schedule_pages[current_page - 1][0][1]))
                 } | Vs. | {schedule_pages[current_page - 1][0][2] + " "*(20 -len(schedule_pages[current_page - 1][0][2]))
                            } | {schedule_pages[current_page - 1][0][3] + " "*(10 -len(schedule_pages[current_page - 1][0][3]))
                                 } | {schedule_pages[current_page - 1][0][4] + " "*(10 -len(schedule_pages[current_page - 1][0][4]))
                                      } | {schedule_pages[current_page - 1][0][5] + " "*(20 -len(schedule_pages[current_page - 1][0][5]))} |\t\t\t\t|
|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|"""
            
            center_list_text = f"""|\t\t\t\t| {schedule_pages[current_page - 1][1][0] + " "*(8 -len(schedule_pages[current_page - 1][1][0]))
            } | {schedule_pages[current_page - 1][1][1] + " "*(20 -len(schedule_pages[current_page - 1][1][1]))
                 } | Vs. | {schedule_pages[current_page - 1][1][2] + " "*(20 -len(schedule_pages[current_page - 1][1][2]))
                            } | {schedule_pages[current_page - 1][1][3] + " "*(10 -len(schedule_pages[current_page - 1][1][3]))
                                 } | {schedule_pages[current_page - 1][1][4] + " "*(10 -len(schedule_pages[current_page - 1][1][4]))
                                      } | {schedule_pages[current_page - 1][1][5] + " "*(20 -len(schedule_pages[current_page - 1][1][5]))} |\t\t\t\t|
|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t| {schedule_pages[current_page - 1][2][0] + " "*(8 -len(schedule_pages[current_page - 1][2][0]))
            } | {schedule_pages[current_page - 1][2][1] + " "*(20 -len(schedule_pages[current_page - 1][2][1]))
                 } | Vs. | {schedule_pages[current_page - 1][2][2] + " "*(20 -len(schedule_pages[current_page - 1][2][2]))
                            } | {schedule_pages[current_page - 1][2][3] + " "*(10 -len(schedule_pages[current_page - 1][2][3]))
                                 } | {schedule_pages[current_page - 1][2][4] + " "*(10 -len(schedule_pages[current_page - 1][2][4]))
                                      } | {schedule_pages[current_page - 1][2][5] + " "*(20 -len(schedule_pages[current_page - 1][2][5]))} |\t\t\t\t|
|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t| {schedule_pages[current_page - 1][3][0] + " "*(8 -len(schedule_pages[current_page - 1][3][0]))
            } | {schedule_pages[current_page - 1][3][1] + " "*(20 -len(schedule_pages[current_page - 1][3][1]))
                 } | Vs. | {schedule_pages[current_page - 1][3][2] + " "*(20 -len(schedule_pages[current_page - 1][3][2]))
                            } | {schedule_pages[current_page - 1][3][3] + " "*(10 -len(schedule_pages[current_page - 1][3][3]))
                                 } | {schedule_pages[current_page - 1][3][4] + " "*(10 -len(schedule_pages[current_page - 1][3][4]))
                                      } | {schedule_pages[current_page - 1][3][5] + " "*(20 -len(schedule_pages[current_page - 1][3][5]))} |\t\t\t\t|
|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t| {schedule_pages[current_page - 1][4][0] + " "*(8 -len(schedule_pages[current_page - 1][4][0]))
            } | {schedule_pages[current_page - 1][4][1] + " "*(20 -len(schedule_pages[current_page - 1][4][1]))
                 } | Vs. | {schedule_pages[current_page - 1][4][2] + " "*(20 -len(schedule_pages[current_page - 1][4][2]))
                            } | {schedule_pages[current_page - 1][4][3] + " "*(10 -len(schedule_pages[current_page - 1][4][3]))
                                 } | {schedule_pages[current_page - 1][4][4] + " "*(10 -len(schedule_pages[current_page - 1][4][4]))
                                      } | {schedule_pages[current_page - 1][4][5] + " "*(20 -len(schedule_pages[current_page - 1][4][5]))} |\t\t\t\t|
|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t| {schedule_pages[current_page - 1][5][0] + " "*(8 -len(schedule_pages[current_page - 1][5][0]))
            } | {schedule_pages[current_page - 1][5][1] + " "*(20 -len(schedule_pages[current_page - 1][5][1]))
                 } | Vs. | {schedule_pages[current_page - 1][5][2] + " "*(20 -len(schedule_pages[current_page - 1][5][2]))
                            } | {schedule_pages[current_page - 1][5][3] + " "*(10 -len(schedule_pages[current_page - 1][5][3]))
                                 } | {schedule_pages[current_page - 1][5][4] + " "*(10 -len(schedule_pages[current_page - 1][5][4]))
                                      } | {schedule_pages[current_page - 1][5][5] + " "*(20 -len(schedule_pages[current_page - 1][5][5]))} |\t\t\t\t|""" 
            
            bottum_list_text = f"""|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t| {schedule_pages[current_page - 1][6][0] + " "*(8 -len(schedule_pages[current_page - 1][6][0]))
            } | {schedule_pages[current_page - 1][6][1] + " "*(20 -len(schedule_pages[current_page - 1][6][1]))
                 } | Vs. | {schedule_pages[current_page - 1][6][2] + " "*(20 -len(schedule_pages[current_page - 1][6][2]))
                            } | {schedule_pages[current_page - 1][6][3] + " "*(10 -len(schedule_pages[current_page - 1][6][3]))
                                 } | {schedule_pages[current_page - 1][6][4] + " "*(10 -len(schedule_pages[current_page - 1][6][4]))
                                      } | {schedule_pages[current_page - 1][6][5] + " "*(20 -len(schedule_pages[current_page - 1][6][5]))} |\t\t\t\t|
|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t| {schedule_pages[current_page - 1][7][0] + " "*(8 -len(schedule_pages[current_page - 1][7][0]))
            } | {schedule_pages[current_page - 1][7][1] + " "*(20 -len(schedule_pages[current_page - 1][7][1]))
                 } | Vs. | {schedule_pages[current_page - 1][7][2] + " "*(20 -len(schedule_pages[current_page - 1][7][2]))
                            } | {schedule_pages[current_page - 1][7][3] + " "*(10 -len(schedule_pages[current_page - 1][7][3]))
                                 } | {schedule_pages[current_page - 1][7][4] + " "*(10 -len(schedule_pages[current_page - 1][7][4]))
                                      } | {schedule_pages[current_page - 1][7][5] + " "*(20 -len(schedule_pages[current_page - 1][7][5]))} |\t\t\t\t|
|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t| {schedule_pages[current_page - 1][8][0] + " "*(8 -len(schedule_pages[current_page - 1][8][0]))
            } | {schedule_pages[current_page - 1][8][1] + " "*(20 -len(schedule_pages[current_page - 1][8][1]))
                 } | Vs. | {schedule_pages[current_page - 1][8][2] + " "*(20 -len(schedule_pages[current_page - 1][8][2]))
                            } | {schedule_pages[current_page - 1][8][3] + " "*(10 -len(schedule_pages[current_page - 1][8][3]))
                                 } | {schedule_pages[current_page - 1][8][4] + " "*(10 -len(schedule_pages[current_page - 1][8][4]))
                                      } | {schedule_pages[current_page - 1][8][5] + " "*(20 -len(schedule_pages[current_page - 1][8][5]))} |\t\t\t\t|
|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t| {schedule_pages[current_page - 1][9][0] + " "*(8 -len(schedule_pages[current_page - 1][9][0]))
            } | {schedule_pages[current_page - 1][9][1] + " "*(20 -len(schedule_pages[current_page - 1][9][1]))
                 } | Vs. | {schedule_pages[current_page - 1][9][2] + " "*(20 -len(schedule_pages[current_page - 1][9][2]))
                            } | {schedule_pages[current_page - 1][9][3] + " "*(10 -len(schedule_pages[current_page - 1][9][3]))
                                 } | {schedule_pages[current_page - 1][9][4] + " "*(10 -len(schedule_pages[current_page - 1][9][4]))
                                      } | {schedule_pages[current_page - 1][9][5] + " "*(20 -len(schedule_pages[current_page - 1][9][5]))} |\t\t\t\t|
|\t\t\t\t+----------+----------------------+-----+----------------------+------------+------------+----------------------+\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""



            if(len(schedule_pages) <= 1):
                up_down_command = """|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""

            elif(current_page == 1):
                up_down_command = """|\t\t\t\t\t\t\t|                  d. to go down the list                     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""

            elif(len(schedule_pages) == current_page):
                up_down_command = """|\t\t\t\t\t\t\t|                   u. to go up the list                      |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""
                
            elif(len(schedule_pages) > current_page and current_page > 1):
                    up_down_command ="""|\t\t\t\t\t\t\t| u. to go up the list        | d. to go down the list        |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""

            footer_text = f"""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                  Enter command you want...                  |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
{up_down_command}
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""

            clear_screen()

            print(header_text)
            print(top_list_text)
            print(center_list_text)
            print(bottum_list_text)
            print(footer_text)

            choice = str(input(">>>> "))

            if(choice.lower() == "u" and 1 < current_page):
                current_page -= 1
            elif(choice.lower() == "d" and len(schedule_pages) > current_page):
                current_page += 1
            elif(choice.lower() == "b"):
                return "BACK"
            elif(choice.lower() == "q"):
                return "QUIT"
            else:
                clear_screen()

                print(header_text)
                print(top_list_text)
                print(error_text)
                print(bottum_list_text)
                print(footer_text)

                choice = str(input(">>>> "))
                if(choice.lower() == "q"):
                    return "BACK"