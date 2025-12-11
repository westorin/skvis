from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper
from main.logic.tournamentsList import TournamentsListLogic
from main.logic.clearScreenInTerminal import clear_screen

class OnGoingTournamentsUI():
    def __init__(self):
        pass


    def print_tournaments(self) -> None:
        data = DataWrapper()
        logic = LogicWrapper(data)
        tm = logic.tournament_manager

        tournaments_list = TournamentsListLogic().sort_on_going_tournaments_list()

        current_page = 1

        header_text = f"""+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t+----------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| ╔═╗┌┐┌  ╔═╗┌─┐┬┌┐┌┌─┐  ╔╦╗┌─┐┬ ┬┬─┐┌┐┌┌─┐┌┬┐┌─┐┌┐┌┌┬┐┌─┐ |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| ║ ║│││  ║ ╦│ ││││││ ┬   ║ │ ││ │├┬┘│││├─┤│││├┤ │││ │ └─┐ |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| ╚═╝┘└┘  ╚═╝└─┘┴┘└┘└─┘   ╩ └─┘└─┘┴└─┘└┘┴ ┴┴ ┴└─┘┘└┘ ┴ └─┘ |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+----------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t|  Name of tournament  | Start date | End date   |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+======================+============+============+\t\t\t\t\t\t\t\t|""" 
        
        error_text ="""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     \x1b[33m^\x1b[0m                                                       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|    \x1b[33m/ \ \x1b[0m       You have entered an invalied input            |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   \x1b[33m/\x1b[0m \033[31m\033[1m|\033[0m \x1b[33m\ \x1b[0m                                                    |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|  \x1b[33m/\x1b[0m  \033[31m\033[1m.\033[0m  \x1b[33m\  \x1b[0m   Enter Y. if you want to try again              |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| \x1b[33m/_______\ \x1b[0m       or q. if you want to quit.                 |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""

        while True:

            top_of_list=f"""|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][0][0] + " "*(20-len(tournaments_list[current_page - 1][0][0]))
                                            } | {tournaments_list[current_page - 1][0][1] + " "*(10-len(tournaments_list[current_page - 1][0][1]))
                                                 } | {tournaments_list[current_page - 1][0][2] + " "*(10-len(tournaments_list[current_page - 1][0][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][1][0] + " "*(20-len(tournaments_list[current_page - 1][1][0]))
   } | {tournaments_list[current_page - 1][1][1] + " "*(10-len(tournaments_list[current_page - 1][1][1]))
        } | {tournaments_list[current_page - 1][1][2]  + " "*(10-len(tournaments_list[current_page - 1][1][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][2][0] + " "*(20-len(tournaments_list[current_page - 1][2][0]))
   } | {tournaments_list[current_page - 1][2][1] + " "*(10-len(tournaments_list[current_page - 1][2][1]))
        } | {tournaments_list[current_page - 1][2][2] + " "*(10-len(tournaments_list[current_page - 1][2][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|""" 
        
            center_list = f"""|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][3][0] + " "*(20-len(tournaments_list[current_page - 1][3][0]))
   } | {tournaments_list[current_page - 1][3][1] + " "*(10-len(tournaments_list[current_page - 1][3][1]))
        } | {tournaments_list[current_page - 1][3][2] + " "*(10-len(tournaments_list[current_page - 1][3][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][4][0] + " "*(20-len(tournaments_list[current_page - 1][4][0]))
   } | {tournaments_list[current_page - 1][4][1] + " "*(10-len(tournaments_list[current_page - 1][4][1]))
        } | {tournaments_list[current_page - 1][4][2] + " "*(10-len(tournaments_list[current_page - 1][4][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][5][0] + " "*(20-len(tournaments_list[current_page - 1][5][0]))
   } | {tournaments_list[current_page - 1][5][1] + " "*(10-len(tournaments_list[current_page - 1][5][1]))
        } | {tournaments_list[current_page - 1][5][2] + " "*(10-len(tournaments_list[current_page - 1][5][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][5][0] + " "*(20-len(tournaments_list[current_page - 1][5][0]))
   } | {tournaments_list[current_page - 1][5][1] + " "*(10-len(tournaments_list[current_page - 1][5][1]))
        } | {tournaments_list[current_page - 1][5][2] + " "*(10-len(tournaments_list[current_page - 1][5][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][6][0] + " "*(20-len(tournaments_list[current_page - 1][6][0]))
   } | {tournaments_list[current_page - 1][6][1] + " "*(10-len(tournaments_list[current_page - 1][6][1]))
        } | {tournaments_list[current_page - 1][6][2] + " "*(10-len(tournaments_list[current_page - 1][6][2]))} |\t\t\t\t\t\t\t\t|""" 
        
            bottum_list =f"""|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][7][0] + " "*(20-len(tournaments_list[current_page - 1][7][0]))
   } | {tournaments_list[current_page - 1][7][1] + " "*(10-len(tournaments_list[current_page - 1][7][1]))
        } | {tournaments_list[current_page - 1][7][2] + " "*(10-len(tournaments_list[current_page - 1][7][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][8][0] + " "*(20-len(tournaments_list[current_page - 1][8][0]))
   } | {tournaments_list[current_page - 1][8][1] + " "*(10-len(tournaments_list[current_page - 1][8][1]))
        } | {tournaments_list[current_page - 1][8][2] + " "*(10-len(tournaments_list[current_page - 1][8][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| {tournaments_list[current_page - 1][9][0] + " "*(20-len(tournaments_list[current_page - 1][9][0]))
   } | {tournaments_list[current_page - 1][9][1] + " "*(10-len(tournaments_list[current_page - 1][9][1]))
        } | {tournaments_list[current_page - 1][9][2] + " "*(10-len(tournaments_list[current_page - 1][9][2]))} |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+----------------------+------------+------------+\t\t\t\t\t\t\t\t|"""
            if(len(tournaments_list) <= 1):
                up_down_command = """|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""

            elif(current_page == 1):
                up_down_command = """|\t\t\t\t\t\t\t|                  d. to go down the list                     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""

            elif(len(tournaments_list) == current_page):
                up_down_command = """|\t\t\t\t\t\t\t|                   u. to go up the list                      |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""
                
            elif(len(tournaments_list) > current_page and current_page > 1):
                up_down_command ="""|\t\t\t\t\t\t\t| u. to go up the list        | d. to go down the list        |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|"""

            footer_text = f"""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   Enter command or the name of the tournament you want...   |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
{up_down_command}
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""

        

            clear_screen()
            print(header_text)
            print(top_of_list)
            print(center_list)
            print(bottum_list)
            print(footer_text)
            choice = str(input(">>>> "))
               
               
            if(choice.lower() == "u" and 1 < current_page):
                current_page -= 1
            elif(choice.lower() == "d" and len(tournaments_list) > current_page):
                current_page += 1
            elif(choice.lower() == "b"):
                return "BACK"
            elif(choice.lower() == "q"):
                return "QUIT"
            else:
                clear_screen()
                print(header_text)
                print(top_of_list)
                print(error_text)
                print(bottum_list)
                print(footer_text)

                choice = str(input(">>>> "))

                if(choice.lower() == "q"):
                    return "BACK"