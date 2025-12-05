import os


print( "Hello world")

name = input("Enter name: ")


def clear_terminal():
    # Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # macOS and Linux
    else:
        _ = os.system('clear')





print("The terminal has been cleared, and this is new text.")

print(f"your name is {name}")