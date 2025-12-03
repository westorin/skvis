import os

# Clears the terminal screen
def clear_screen():
    # Checks what os you're using and if it is windows
    if os.name == "nt":
        # it will run cls in your terminal
        os.system("cls")
    else:
        # And if your os isn't windows it will run clear in your terminal
        os.system("clear")
