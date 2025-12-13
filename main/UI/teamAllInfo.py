from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

from main.logic.team import TeamLogic #<-- This has to go
from main.logic.clearScreenInTerminal import clear_screen
import math


class TeamAllInfoUI():
    def __init__(self, logic):
        self.logic = logic 
        #Need to add: logic in the init
        data = DataWrapper() #<-- This can go
        logic = LogicWrapper(data) #<-- This can go
        #self.logic = logic
        #Add the line above
        self.player = logic.player_manager
        self.team = logic.team_manager


    def print_team_info(self, team_name: str, isAAdmin: bool, isATeamCapt: bool) -> str:
        self.team_name = team_name
        isAAdmin = isAAdmin
        isATeamCapt = isATeamCapt
        logic_team = TeamLogic(self).create_list_of_teams_all_info(self.team_name)
        wins = "" 
        win_rate = ""
        losses = ""

        if(isAAdmin == True and len(logic_team[0][3]) < 5 and len(logic_team[0][3]) > 3):
            commands = """|\t\t\t\t\t\t\t+=====================+================+======================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| u. Update a player  | a. Add player  | r. Remove a player   |\t\t\t\t\t\t\t\t|"""
        
        elif(isAAdmin == True and len(logic_team[0][3]) >= 5):
            commands = """|\t\t\t\t\t\t\t+=============================+===============================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| u. Update a player          | r. Remove a player            |\t\t\t\t\t\t\t\t|"""
        
        elif(isAAdmin == True and len(logic_team[0][3]) <= 3):
            commands = """|\t\t\t\t\t\t\t+=============================+===============================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| u. Update a player          | a. Add a player               |\t\t\t\t\t\t\t\t|"""
        
        elif(isATeamCapt == True and len(logic_team[0][3]) < 5 and len(logic_team[0][3]) > 3):
            commands = """|\t\t\t\t\t\t\t+=============================+===============================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| a. Add player               | r. Remove a player            |\t\t\t\t\t\t\t\t|"""
        elif(isATeamCapt == True and len(logic_team[0][3]) >= 5):
            commands = """|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                    r. Remove a player                       |\t\t\t\t\t\t\t\t|"""
        elif(isATeamCapt == True and len(logic_team[0][3]) <= 3):
            commands = """|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                      a. Add a player                        |\t\t\t\t\t\t\t\t|"""

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
|\t\t+----------------------+----------------------+---------------+----------------------+-----------+----------------------+----------------------+\t\t|
|\t\t| Name                 | Username             | Date of birth | address              | Phone nr. | Email                | URL                  |\t\t|
|\t\t+======================+======================+===============+======================+===========+======================+======================+\t\t|
|\t\t| {logic_team[1][0] + " "*(20 -len(logic_team[1][0]))
        } | {logic_team[1][1] + " "*(20 -len(logic_team[1][1]))
             } | {logic_team[1][2] + " "*(13 -len(logic_team[1][2]))
                  } | {logic_team[1][3] + " "*(20 -len(logic_team[1][3]))
                       } | {logic_team[1][4] + " "*(9 -len(logic_team[1][4]))
                            } | {logic_team[1][5] + " "*(20 -len(logic_team[1][5]))
                                 } | {logic_team[1][6] + " "*(20 -len(logic_team[1][6]))} |\t\t|
|\t\t+----------------------+----------------------+---------------+----------------------+-----------+----------------------+----------------------+\t\t|
|\t\t| {logic_team[2][0] + " "*(20 -len(logic_team[2][0]))
        } | {logic_team[2][1] + " "*(20 -len(logic_team[2][1]))
             } | {logic_team[2][2] + " "*(13 -len(logic_team[2][2]))
                  } | {logic_team[2][3] + " "*(20 -len(logic_team[2][3]))
                       } | {logic_team[2][4] + " "*(9 -len(logic_team[2][4]))
                            } | {logic_team[2][5] + " "*(20 -len(logic_team[2][5]))
                                 } | {logic_team[2][6] + " "*(20 -len(logic_team[2][6]))} |\t\t|
|\t\t+----------------------+----------------------+---------------+----------------------+-----------+----------------------+----------------------+\t\t|
|\t\t| {logic_team[3][0] + " "*(20 -len(logic_team[3][0]))
        } | {logic_team[3][1] + " "*(20 -len(logic_team[3][1]))
             } | {logic_team[3][2] + " "*(13 -len(logic_team[3][2]))
                  } | {logic_team[3][3] + " "*(20 -len(logic_team[3][3]))
                       } | {logic_team[3][4] + " "*(9 -len(logic_team[3][4]))
                            } | {logic_team[3][5] + " "*(20 -len(logic_team[3][5]))
                                 } | {logic_team[3][6] + " "*(20 -len(logic_team[3][6]))} |\t\t|
|\t\t+----------------------+----------------------+---------------+----------------------+-----------+----------------------+----------------------+\t\t|"""
        center_text = f"""|\t\t| {logic_team[4][0] + " "*(20 -len(logic_team[4][0]))
        } | {logic_team[4][1] + " "*(20 -len(logic_team[4][1]))
             } | {logic_team[4][2] + " "*(13 -len(logic_team[4][2]))
                  } | {logic_team[4][3] + " "*(20 -len(logic_team[4][3]))
                       } | {logic_team[4][4] + " "*(9 -len(logic_team[4][4]))
                            } | {logic_team[4][5] + " "*(20 -len(logic_team[4][5]))
                                 } | {logic_team[4][6] + " "*(20 -len(logic_team[4][6]))} |\t\t|
|\t\t+----------------------+----------------------+---------------+----------------------+-----------+----------------------+----------------------+\t\t|
|\t\t| {logic_team[5][0] + " "*(20 -len(logic_team[5][0]))
        } | {logic_team[5][1] + " "*(20 -len(logic_team[5][1]))
             } | {logic_team[5][2] + " "*(13 -len(logic_team[5][2]))
                  } | {logic_team[5][3] + " "*(20 -len(logic_team[5][3]))
                       } | {logic_team[5][4] + " "*(9 -len(logic_team[5][4]))
                            } | {logic_team[5][5] + " "*(20 -len(logic_team[5][5]))
                                 } | {logic_team[5][6] + " "*(20 -len(logic_team[5][6]))} |\t\t|
|\t\t+----------------------+----------------------+---------------+----------------------+-----------+----------------------+----------------------+\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""
        footer_text = f"""|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|       Enter a command or the username you want...           |\t\t\t\t\t\t\t\t|
{commands}
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
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

        if(choice.lower() == "q"):
            return "QUIT"
        elif(choice.lower() == "b"):
            return "BACK"
        elif(choice.lower() == "a" and (isAAdmin == True or isATeamCapt == True)):
            return "ADD_PLAYER_TO_TEAM", team_name
        elif(choice.lower() == "u" and isAAdmin == True):
            username_input = ""
            command_for_user_change = "JUST_BACK"
            while True:
                if(command_for_user_change == "JUST_BACK"):
                    change_commands = """|\t\t\t\t\t\t\t+=====+===============================================+=======+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                     b. Go back                              |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""
                
                elif(command_for_user_change == "BACK_CHANGE_USER_ENTER"):
                    change_commands = """|\t\t\t\t\t\t\t+=====+===================+==================+========+=======+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| d. enter diffrent user  | e. Update user   | b. Go back     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------+------------------+----------------+\t\t\t\t\t\t\t\t|"""

                user_input_text =f"""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                   Enter the username...                     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|       username:                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     +-----------------------------------------------+       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     | {username_input + " "*(45 -len(username_input)) } |       |\t\t\t\t\t\t\t\t|
{change_commands}"""
                
                print(header_text)
                print(user_input_text)
                print(footer_text)

                choice = str(input(">>>> "))

                if(choice.lower() == "b"):
                    break
                elif(username_input == "" and len(choice) < 46):
                    username_input = choice
                    command_for_user_change = "BACK_CHANGE_USER_ENTER"
                elif(command_for_user_change == "BACK_CHANGE_USER_ENTER" and choice.lower() == "d"):
                    username_input = ""
                    command_for_user_change = "JUST_BACK"
                elif(command_for_user_change == "BACK_CHANGE_USER_ENTER" and choice.lower() == "e" and self.player.does_player_exist(username_input) == True):
                    return "UPDATE_PLAYER", username_input
                else:
                    clear_screen()

                    print(header_text)
                    print(error_text)
                    print(footer_text)

                    choice = str(input(">>>> "))

                    if(choice.lower() == "q"):
                        return "BACK"

        elif(choice.lower() == "r" and (isAAdmin == True or isATeamCapt == True)):
            username_input = ""
            command_for_user_change = "JUST_BACK"
            while True:
                if(command_for_user_change == "JUST_BACK"):
                    change_commands = """|\t\t\t\t\t\t\t+=====+===============================================+=======+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                     b. Go back                              |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""
                
                elif(command_for_user_change == "BACK_CHANGE_USER_ENTER"):
                    change_commands = """|\t\t\t\t\t\t\t+=====+===================+==================+========+=======+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| d. enter diffrent user  | e. Remove user   | b. Go back     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------+------------------+----------------+\t\t\t\t\t\t\t\t|"""

                user_input_text =f"""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                   Enter the username...                     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|       username:                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     +-----------------------------------------------+       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     | {username_input + " "*(45 -len(username_input)) } |       |\t\t\t\t\t\t\t\t|
{change_commands}"""
                
                print(header_text)
                print(user_input_text)
                print(footer_text)

                choice = str(input(">>>> "))

                if(choice.lower() == "b"):
                    break
                elif(username_input == "" and len(choice) < 46):
                    username_input = choice
                    command_for_user_change = "BACK_CHANGE_USER_ENTER"
                elif(command_for_user_change == "BACK_CHANGE_USER_ENTER" and choice.lower() == "d"):
                    username_input = ""
                    command_for_user_change = "JUST_BACK"
                elif(command_for_user_change == "BACK_CHANGE_USER_ENTER" and choice.lower() == "e" and self.player.does_player_exist(username_input) == True):
                    self.team.remove_player_from_team(team_name, username_input)
                    break
                else:
                    clear_screen()

                    print(header_text)
                    print(error_text)
                    print(footer_text)

                    choice = str(input(">>>> "))

                    if(choice.lower() == "q"):
                        return "BACK"
                        
        else:
            clear_screen()

            print(header_text)
            print(error_text)
            print(footer_text)

            choice = str(input(">>>> "))

            if(choice.lower() == "q"):
                return "BACK"