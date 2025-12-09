from main.logic.clearScreenInTerminal import clear_screen

class PickTimeOfTournamntsUI():
    def __init__(self):
        pass
    

    def print_ptot_ui(self):

        header_text = """+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
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

        # TODO Shoud entering q in the error massage sent to back or close the program ???? 
        error_text ="""|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     ^                                                       |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|    / \       You have entered an invalied input             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|   / | \                                                     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|  /  .  \     Enter Y. if you want to try again              |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| /_______\        or q. if you want to quit.                 |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                                                             |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|"""

        center_text = """|\t\t\t\t\t\t\t                          **************   *                   \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          *************                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                         **************                        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                             *****                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t                          e-Sports                             \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-------------------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                 Enter the command you want...               |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+====================+===================+====================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                    |                   |                    |\t\t\t\t\t\t\t\t|"""

        footer_text = """|\t\t\t\t\t\t\t|   1.   Past        |  2. Ongoing       | 3.  Future         |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|     tournaments    |    tournamets     |    tournaments     |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|                    |                   |                    |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+====================+========+==========+====================+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t|         b. To go back       |    q. To quit  the program    |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+-----------------------------+-------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""

        while True:
            clear_screen()

            print(header_text)
            print(center_text)
            print(footer_text)

            choice = str(input(">>>>"))

            if(choice == "1"):
                return "Past"
            elif(choice == "2"):
                return "Ongoing"
            elif(choice == "3"):
                return "Future"
            elif(choice.lower() == "b"):
                return "BACK"
            elif choice.lower() == "q":
                return "QUIT"
            else:
                clear_screen()

                print(header_text)
                print(error_text)
                print(footer_text)
                
                choice_error = input(">>>>")
                if(choice_error.lower() == "q"):
                    return "BACK"