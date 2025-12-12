import os
import sys

def clear_screen():
    if sys.platform.startswith('win'):
        os.system('cls')
    else:
        os.system('clear')

class ClearScreenLogic:
    def clear(self) -> None:
        clear_screen()

