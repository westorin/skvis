'''
To run the main UI type this into terminal: 

python3 -m main.UI.mainUI

'''
from main.UI.createplayerUI import PlayerUI
from main.logic.clearScreenInTerminal import clear_screen
import os

def main():
    player_ui = PlayerUI()

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
|\t\t\t\t\t\t\t| 1. Tournaments     | 2. Leader Board   | 3. teams           |\t\t\t\t\t\t\t\t|"""

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
|\t\t\t\t\t\t\t| 4. clubs           | {var1} | 6. players         |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t+--------------------+-------------------+--------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| {var2} | 8. search         |                    |\t\t\t\t\t\t\t\t|
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

        choice = input(">>>>")

        if choice == "1":
            player_ui.register_player_ui()
        elif choice.lower() == "q":
            break
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

if __name__ == "__main__":
    main()