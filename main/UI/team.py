from main.logic.team import TeamLogic
from main.logic.clearScreenInTerminal import clear_screen
import math


class TeamUI():
    def __init__(self):
        pass

    def print_team(self, team_name: str) -> str:
        self.team_name = team_name
        logic_team = TeamLogic(self).create_list_of_team_info_for_all(self.team_name)
        wins = "" 
        win_rate = ""
        losses = ""        

        header_text = f"""+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         +------------------------------------------+          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         | {" "*math.floor((40 -len(logic_team[0][0]))/2) + logic_team[0][0] + " "*math.ceil((40 -len(logic_team[0][0]))/2)} |          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         +------------------------------------------+          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t    +----------------------+----------------------+--------+--------+----------+\t\t\t\t\t\t\t|
|\t\t\t\t\t    | Team Captain         | URL.                 |  Wins  | losses | Win rate |\t\t\t\t\t\t\t|
|\t\t\t\t\t    +======================+======================+========+========+==========+\t\t\t\t\t\t\t|
|\t\t\t\t\t    | {logic_team[0][1] + " "*(20 - len(logic_team[0][1]))} | {logic_team[0][2] + " "*(20 -len(logic_team[0][2]))} | {wins + " "*(6 - len(wins))} | {losses + " "*(6 -len(losses))} | {win_rate + " "*(8 -len(win_rate))} |\t\t\t\t\t\t\t|
|\t\t\t\t\t    +----------------------+----------------------+--------+--------+----------+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        | Name                 | Username             |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +======================+======================+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        | {logic_team[1][0] + " "*(20 -len(logic_team[1][0]))} | {logic_team[1][1] + " "*(20 -len(logic_team[1][1]))} |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        | {logic_team[2][0] + " "*(20 -len(logic_team[2][0]))} | {logic_team[2][1] + " "*(20 -len(logic_team[2][1]))} |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        | {logic_team[3][0] + " "*(20 -len(logic_team[3][0]))} | {logic_team[3][1] + " "*(20 -len(logic_team[3][1]))} |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|"""
        center_text = f"""|\t\t\t\t\t\t\t        | {logic_team[4][0] + " "*(20 -len(logic_team[4][0]))} | {logic_team[4][1] + " "*(20 -len(logic_team[4][1]))} |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        | {logic_team[5][0] + " "*(20 -len(logic_team[5][0]))} | {logic_team[5][1] + " "*(20 -len(logic_team[5][1]))} |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""
        footer_text = """|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|       Enter a command or the username you want...           |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+=============================+===============================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| b. To go back               | q. To quit  the program       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""
        error_text ="""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     \x1b[33m^\x1b[0m                                                       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|    \x1b[33m/ \ \x1b[0m       You have entered an invalied input            |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   \x1b[33m/\x1b[0m \033[31m\033[1m|\033[0m \x1b[33m\ \x1b[0m                                                    |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|  \x1b[33m/\x1b[0m  \033[31m\033[1m.\033[0m  \x1b[33m\  \x1b[0m   Enter Y. if you want to try again              |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| \x1b[33m/_______\ \x1b[0m       or q. if you want to quit.                 |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""
        clear_screen()


        print(header_text)
        print(center_text)
        print(footer_text)

        choice = str(input(">>>> "))

        while True:
            if(choice.lower() == "b"):
                return "BACK"
            elif(choice.lower() == "q"):
                return "QUIT"
            else:
                clear_screen()

                print(header_text)
                print(error_text)
                print(footer_text)

                choice = str(input(">>>> "))

                if(choice.lower() == "q"):
                    return "BACK"

