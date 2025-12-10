from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper
from main.repo.playerrepo import PlayerRepository
from main.logic.clearScreenInTerminal import clear_screen



class LoginUI():
    def __init__(self):
        pass

    

    def print_login(self) -> tuple:
        data = DataWrapper()
        logic = LogicWrapper(data)
        pr =PlayerRepository()
        self.login_manager = logic.login_manager
        
        self.username = ""
        self.password = ""

        header_text = """+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                       *****         ***                       \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                     *********************                     \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                   **************************                  \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                 *****************************                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                *******************************                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               *******************************                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t              ********************************                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               **************     ************                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                   ********         ***********                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                   ********         ***********                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                  ***********     ************                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               ******************************                  \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               *********************************               \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                *********   *******************                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                 ****      ************* *****                 \t\t\t\t\t\t\t\t|""" 
        error_text ="""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     ^                                                       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|    / \       You have entered an invalied input             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   / | \                                                     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|  /  .  \     Enter Y. if you want to try again              |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| /_______\        or q. if you want to quit.                 |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""

        while True:
            user_inputs_text = f"""|\t\t\t\t\t\t\t|   +-----------------------------------------------------+   |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   | {self.username + " "*(51 -len(self.username))} |   |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   +-----------------------------------------------------+   |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     Password:                                               |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   +-----------------------------------------------------+   |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   | {"*"*len(self.password) + " "*(51 -len(self.password))} |   |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   +-----------------------------------------------------+   |\t\t\t\t\t\t\t\t|"""
        
            base_commands_text ="""|\t\t\t\t\t\t\t+===================+===============+=========================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| t. try loging in  | b. To go back | q. To quit  the program |\t\t\t\t\t\t\t\t|"""
            if(self.username != "" and self.password != ""):
                change_commands = """|\t\t\t\t\t\t\t+==============================+==============================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| u. To change username input  | p. To change password input  |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------+----------+----+-------------------------+\t\t\t\t\t\t\t\t|"""
                add_space = """"""
                enter_name = "command "
            elif(self.username != ""):
                change_commands = """|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|               u. To change username input                   |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------+---------------+-------------------------+\t\t\t\t\t\t\t\t|"""
                add_space = """"""
                enter_name = "password"
                
            elif(self.password != "" and self.username == ""):
                change_commands = """|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|               p. To change password input                   |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------+---------------+-------------------------+\t\t\t\t\t\t\t\t|"""
                add_space = """"""
                enter_name = "username"
            else:
                change_commands = """|\t\t\t\t\t\t\t+===================+===============+=========================+\t\t\t\t\t\t\t\t|"""
                add_space = """\n|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""
                enter_name = "username"

            center_text = f"""|\t\t\t\t\t\t\t                          **************   *                   \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          *************                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                         **************                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                             *****                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          e-Sports                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                 Enter your {enter_name}                         |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+=============================================================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     Username:                                               |\t\t\t\t\t\t\t\t|"""

            commands_text = f"""{change_commands}
|\t\t\t\t\t\t\t| t. try loging in  | b. To go back | q. To quit  the program |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------+---------------+-------------------------+\t\t\t\t\t\t\t\t|{add_space}
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""

            login_pop_up_text = f"""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|╦ ╦╔═╗╦ ╦  ╦ ╦╔═╗╦  ╦╔═╗  ╔╗ ╔═╗╔═╗╔╗╔  ╦  ╔═╗╔═╗╔═╗╔╦╗  ╦╔╗╔|\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|╚╦╝║ ║║ ║  ╠═╣╠═╣╚╗╔╝║╣   ╠╩╗║╣ ║╣ ║║║  ║  ║ ║║ ╦║╣  ║║  ║║║║|\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| ╩ ╚═╝╚═╝  ╩ ╩╩ ╩ ╚╝ ╚═╝  ╚═╝╚═╝╚═╝╝╚╝  ╩═╝╚═╝╚═╝╚═╝═╩╝  ╩╩╚╝|\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|      AS: {self.username.upper() + " "*(47 - len(self.username))}    |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""

            clear_screen()
            print(header_text)
            print(center_text)
            print(user_inputs_text)
            print(commands_text)
            
            choice = str(input(">>>>"))
            
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
                    choice = str(input(">>>>"))
                    return "ADMIN"
                elif(role == "captain"):
                    team_name = pr.get_by_handle(self.username)
                    clear_screen()
                    print(header_text)
                    print(login_pop_up_text)
                    print(user_inputs_text)
                    print(commands_text)
                    print(team_name.team)
                    choice = str(input(">>>>"))
                    return "CAPT", team_name.team
                else:
                    print("error in the login checker")
                    
            else:
                clear_screen()
                print(header_text)
                print(error_text)
                print(user_inputs_text)
                print(commands_text)
                
                choice = str(input(">>>>"))

                if(choice.lower() == "q"):
                    return "BACK"