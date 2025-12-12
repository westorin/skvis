#UI -> LogicWrapper -> Logic -> Repository -> IO -> CSV
from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper
from main.repo.playerrepo import PlayerRepository #<-- This needs to go
from main.logic.clearScreenInTerminal import clear_screen



class LoginUI():
    def __init__(self, logic) -> None:
        self.logic = logic

    

    def print_login(self) -> tuple:
        data = DataWrapper()
        logic = LogicWrapper(data)
        pr =PlayerRepository() #<-- This needs to go
        self.login_manager = logic.login_manager
        
        self.username = ""
        self.password = ""

        header_text = """+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                       \033[31m\033[1m*****         ***\033[0m                       \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                     \033[31m\033[1m*********************\033[0m                     \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                   \033[31m\033[1m**************************\033[0m                  \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                 \033[31m\033[1m*****************************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                \033[31m\033[1m*******************************\033[0m                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               \033[31m\033[1m*******************************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t              \033[31m\033[1m********************************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               \033[31m\033[1m**************     ************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                   \033[31m\033[1m********         ***********\033[0m                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                   \033[31m\033[1m********         ***********\033[0m                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                  \033[31m\033[1m***********     ************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               \033[31m\033[1m******************************\033[0m                  \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               \033[31m\033[1m*********************************\033[0m               \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                \033[31m\033[1m*********   *******************\033[0m                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                 \033[31m\033[1m****      ************* *****\033[0m                 \t\t\t\t\t\t\t\t|""" 
        
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
            user_inputs_text = f"""|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m   \033[30m\033[1m+-----------------------------------------------------+\033[0m   \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m   \033[30m\033[1m|\033[0m {self.username + " "*(51 -len(self.username))} \033[30m\033[1m|\033[0m   \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m   \033[30m\033[1m+-----------------------------------------------------+\033[0m   \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m     Password:                                               \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m   \033[30m\033[1m+-----------------------------------------------------+\033[0m   \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m   \033[30m\033[1m|\033[0m {"*"*len(self.password) + " "*(51 -len(self.password))} \033[30m\033[1m|\033[0m   \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m   \033[30m\033[1m+-----------------------------------------------------+\033[0m   \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|"""
        
            base_commands_text ="""|\t\t\t\t\t\t\t\033[30m\033[1m+===================+===============+=========================+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m t. try loging in  \033[30m\033[1m|\033[0m b. To go back \033[30m\033[1m|\033[0m q. To quit  the program \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|"""
            
            if(self.username != "" and self.password != ""):
                change_commands = """|\t\t\t\t\t\t\t\033[30m\033[1m+==============================+==============================+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m u. To change username input  \033[30m\033[1m|\033[0m p. To change password input  \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-------------------+----------+----+-------------------------+\033[0m\t\t\t\t\t\t\t\t|"""
                
                add_space = """"""    
                enter_name = "command "
            
            elif(self.username != ""):
                change_commands = """|\t\t\t\t\t\t\t\033[30m\033[1m+=============================================================+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m               u. To change username input                   \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-------------------+---------------+-------------------------+\033[0m\t\t\t\t\t\t\t\t|"""
                
                add_space = """"""
                enter_name = "password"
                
            elif(self.password != "" and self.username == ""):
                change_commands = """|\t\t\t\t\t\t\t\033[30m\033[1m+=============================================================+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m               p. To change password input                   \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-------------------+---------------+-------------------------+\033[0m\t\t\t\t\t\t\t\t|"""
                
                add_space = """"""
                enter_name = "username"

            else:
                change_commands = """|\t\t\t\t\t\t\t\033[30m\033[1m+===================+===============+=========================+\033[0m\t\t\t\t\t\t\t\t|"""
                
                add_space = """\n|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""
                
                enter_name = "username"

            center_text = f"""|\t\t\t\t\t\t\t                          \033[31m\033[1m**************   *\033[0m                   \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          \033[31m\033[1m*************\033[0m                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                         \033[31m\033[1m**************\033[0m                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                             \033[31m\033[1m*****\033[0m                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          \033[31m\033[1m\033[4me-Sports\033[0m                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-------------------------------------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m                 Enter your {enter_name}                         \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+=============================================================+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m     Username:                                               \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|"""

            commands_text = f"""{change_commands}
|\t\t\t\t\t\t\t\033[30m\033[1m|\033[0m t. try loging in  \033[30m\033[1m|\033[0m b. To go back \033[30m\033[1m|\033[0m q. To quit  the program \033[30m\033[1m|\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m\033[1m+-------------------+---------------+-------------------------+\033[0m\t\t\t\t\t\t\t\t|{add_space}
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""

            login_pop_up_text = f"""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|\033[32m\033[1m╦ ╦╔═╗╦ ╦  ╦ ╦╔═╗╦  ╦╔═╗  ╔╗ ╔═╗╔═╗╔╗╔  ╦  ╔═╗╔═╗╔═╗╔╦╗  ╦╔╗╔\033[0m|\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|\033[32m\033[1m╚╦╝║ ║║ ║  ╠═╣╠═╣╚╗╔╝║╣   ╠╩╗║╣ ║╣ ║║║  ║  ║ ║║ ╦║╣  ║║  ║║║║\033[0m|\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|\033[32m\033[1m ╩ ╚═╝╚═╝  ╩ ╩╩ ╩ ╚╝ ╚═╝  ╚═╝╚═╝╚═╝╝╚╝  ╩═╝╚═╝╚═╝╚═╝═╩╝  ╩╩╚╝\033[0m|\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|      AS: {self.username.upper() + " "*(47 - len(self.username))}    |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""

            clear_screen()
            print(header_text)
            print(center_text)
            print(user_inputs_text)
            print(commands_text)
            
            choice = str(input(">>>> "))
            
            if(choice.lower() == "q"):
                return "QUIT"
            elif(choice.lower() == "u" and self.username != ""):
                self.username = ""
            elif(choice.lower() == "p" and self.password != ""):
                self.password = ""
            
            elif(choice.lower() == "b"):
                return "BACK"
            
            elif(len(choice) < 51  and self.username == ""):
                self.username = choice

            elif(len(choice) < 51  and self.password == ""):
                self.password = choice

            elif(choice.lower() == "t"):
                role = self.login_manager.authenticate(self.username, self.password)
                if(role == "admin"):
                    clear_screen()
                    print(header_text)
                    print(login_pop_up_text)
                    print(user_inputs_text)
                    print(commands_text)
                    choice = str(input(">>>> "))
                    return "ADMIN"
                elif(role == "captain"):
                    team_name = pr.get_by_handle(self.username) #<-- This needs to go
                    player = logic.player_manager.get_player_by_handle(self.username)
                    team_name = player.team if player else None
                    #Can replace it with the two lines above
                    clear_screen()
                    print(header_text)
                    print(login_pop_up_text)
                    print(user_inputs_text)
                    print(commands_text)
                    #print(team_name) 
                    # Can replace it with the line above
                    choice = str(input(">>>> "))
                    return "CAPT", team_name 
                    # Can replace it with this line above
                else:
                    print("error in the login checker")
                    
            else:
                clear_screen()
                print(header_text)
                print(error_text)
                print(user_inputs_text)
                print(commands_text)
                
                choice = str(input(">>>> "))

                if(choice.lower() == "q"):
                    return "BACK"