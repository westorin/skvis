from main.logic.clearScreenInTerminal import clear_screen

class homepageUI():
    def __init__(self):
        pass

    def print_menu(self):
        # This checks if you are signed in as admin and prints out what you should see according to it
        admin = False
        if admin == True:
            var1 = "5. Sign Out      "
            var2 = "7. Add tournament "
        else:
            var1 = "5. Login         "
            var2 = "                  "
        
        header = """+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
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

        center_text = """|\t\t\t\t\t\t\t                          **************   *                   \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          *************                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                         **************                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                             *****                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          e-Sports                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
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
                return "Leader Board"
            elif(choice == "3"):
                return "Teams"
            elif(choice == "4"):
                return "Clubs"
            elif(choice == "5"):
                if(admin == True):
                    return "Sign out"
                else:
                    return "Login"
            elif(choice == "6"):
                return "Players"
            elif(choice == "7" and admin == True):
                return "Add tournament"
            elif(choice == "8"):
                return "Search"
            elif choice.lower() == "q":
                return "QUIT"
            else:
                clear_screen()

                print(header)
                print(error_text)
                print(footer)
                
                choice_error = input(">>>>")
                if( choice_error.lower() == "q"):
                    break
                else:
                    clear_screen()
