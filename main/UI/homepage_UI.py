from main.logic.clearScreenInTerminal import clear_screen

class homepageUI():
    def __init__(self):
        pass

    def print_menu(self, isAdminFromMainUI: bool, isATeamCaptFromMainUI: bool):
        # This checks if you are signed in as admin and prints out what you should see according to it
        self.isAdmin = isAdminFromMainUI
        self.isATeamCapt = isATeamCaptFromMainUI

        if(self.isAdmin == True or self.isATeamCapt == True):
            var1 = "5. Sign Out      "
            if(self.isAdmin == True):
                var2 = "7. Add tournament "
            else:
                var2 = "                  "
        else:
            var1 = "5. Login         "
            var2 = "                  "
        
        header = """+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                       \033[31m*****         ***\033[0m                       \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                     \033[31m*********************\033[0m                     \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                   \033[31m**************************\033[0m                  \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                 \033[31m*****************************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                \033[31m*******************************\033[0m                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               \033[31m*******************************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t              \033[31m********************************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               \033[31m**************     ************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                   \033[31m********         ***********\033[0m                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                   \033[31m********         ***********\033[0m                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                  \033[31m***********     ************\033[0m                 \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               \033[31m******************************\033[0m                  \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t               \033[31m*********************************\033[0m               \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                \033[31m*********   *******************\033[0m                \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                 \033[31m****      ************* *****\033[0m                 \t\t\t\t\t\t\t\t|""" 

        center_text = """|\t\t\t\t\t\t\t                          \033[31m**************   *\033[0m                   \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          \033[31m*************\033[0m                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                         \033[31m**************\033[0m                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                             \033[31m*****\033[0m                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          \033[31m\033[1mE-SPORTS\033[0m                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\033[30m+-------------------------------------------------------------+\033[0m\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                 Enter the command you want...               |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+====================+===================+====================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| 1. Tournaments     | 2. Leader Board   | 3. Teams           |\t\t\t\t\t\t\t\t|"""

        error_text ="""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     ^                                                       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|    / \       You have entered an invalied input             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   / | \                                                     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|  /  .  \     Enter Y. if you want to try again              |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| /_______\        or q. if you want to quit.                 |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""

        footer = f"""|\t\t\t\t\t\t\t+--------------------+-------------------+--------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| 4. Clubs           | {var1} | 6. Players         |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+--------------------+-------------------+--------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| {var2} | 8. Search         |                    |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+====================+===================+====================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                         q. quit                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""
        while True:
            clear_screen()

            print(header)
            print(center_text)
            print(footer)

            choice = str(input(">>>>"))

            if choice == "1":
                return "TIME"
            elif(choice == "2"):
                return "LEADER"
            elif(choice == "3"):
                return "TEAMS"
            elif(choice == "4"):
                return "CLUBS"
            elif(choice == "5"):
                if(self.isAdmin == True or self.isATeamCapt == True):
                    return "SIGN"
                else:
                    return "LOGIN"
            elif(choice == "6"):
                return "PLAYERS"
            elif(choice == "7" and self.isAdmin == True):
                return "ADD"
            elif(choice == "8"):
                return "SEARCH"
            elif choice.lower() == "q":
                return "QUIT"
            else:
                clear_screen()

                print(header)
                print(error_text)
                print(footer)
                
                choice_error = input(">>>>")
                if( choice_error.lower() == "q"):
                    return "QUIT"
                else:
                    clear_screen()
