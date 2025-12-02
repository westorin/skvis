'''
To run the main UI type this into terminal: 

python -m main.UI.mainUI

'''
from main.UI.createplayerUI import PlayerUI

def main():
    player_ui = PlayerUI()

    while True:
        print("\n=== MAIN MENU ===")
        print("1. Register Player")
        print("9. Quit")

        choice = input("Choose: ")

        if choice == "1":
            player_ui.register_player_ui()
        elif choice == "9":
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()