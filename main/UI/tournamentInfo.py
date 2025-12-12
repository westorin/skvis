from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper
from main.logic.clearScreenInTerminal import clear_screen
import math

class TournamentInfoUI():
    def __init__(self, logic):
        self.logic = logic

    def print_info(self, tournament_name: str, is_admin: bool):
        data = DataWrapper()
        logic = LogicWrapper(data)

        tour_data = data.tournaments.get_by_name(tournament_name)

        header_text = f"""+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         +------------------------------------------+          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         | {" "*math.floor((40 -len(tour_data.name)) /2) + tour_data.name + " "*math.ceil((40 -len(tour_data.name)) /2)} |          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         +------------------------------------------+          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+------------------------------------------+------------+------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|          Locaion of tournament           | Start date |  End date  |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+==========================================+============+============+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| {" "*math.floor((40 -len(tour_data.location)) /2) + tour_data.location + " "*math.ceil((40 -len(tour_data.location)) /2)} | {tour_data.start} | {tour_data.end} |\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+------------------------------------------+------------+------------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""
        
        center_text = """|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""

        error_text ="""|\t\t\t\t\t\t+------------------------------------------------------------------------------+\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                              |\t\t\t\t\t\t|
|\t\t\t\t\t\t|     ^                                                                        |\t\t\t\t\t\t|
|\t\t\t\t\t\t|    / \             You have entered an invalid input                         |\t\t\t\t\t\t|
|\t\t\t\t\t\t|   / | \                                                                      |\t\t\t\t\t\t|
|\t\t\t\t\t\t|  /  .  \            Enter Y. if you want to try again                        |\t\t\t\t\t\t|
|\t\t\t\t\t\t| /_______\               or q. if you want to quit.                           |\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                              |\t\t\t\t\t\t|
|\t\t\t\t\t\t+------------------------------------------------------------------------------+\t\t\t\t\t\t|"""

        if( is_admin == True):
            command_text = f"""\n|\t\t\t\t\t\t\t\t+------------------------------------------+\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t|             4. Update Match              |\t\t\t\t\t\t\t\t\t|"""
            pading_text = f""""""
        else:
            command_text = f""""""
            pading_text = f"""\n|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""


        footer_text =f"""|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+------------------------------------------+\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t|              Enter command               |\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+==========================================+\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t|          1. Show games schedule          |\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+------------------------------------------+\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t|         2. Display leader board          |\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+------------------------------------------+\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t|     3. Display game by game results      |\t\t\t\t\t\t\t\t\t|{command_text}
|\t\t\t\t\t\t\t\t+====================+=====================+\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| b. go to last page | q. Quit the program |\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+--------------------+---------------------+\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|{pading_text}
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""

        while True:

            clear_screen()

            print(header_text)
            print(center_text)
            print(footer_text)
            choice = str(input(">>>> "))

            if(choice.lower() == "q"):
                return "QUIT"
            elif(choice.lower() == "b"):
                return "BACK"
            elif(choice == "1"):
                return "SCHEDULE"
            elif(choice == "2"):
                return "TOUR_LEADER"
            elif(choice == "3"):
                return "GAME_BY_GAME"
            elif(choice == "4"):
                return "UPDATE_MATCH"
            else:
                
                clear_screen()

                print(header_text)
                print(error_text)
                print(footer_text)

                choice = str(input(">>>> "))

                if(choice.lower() == "q"):
                    return "BACK"
            