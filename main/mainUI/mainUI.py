import os


print( "Hello world")

name = input("Enter name: ")


def clear_terminal():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

# Example usage:
print("This text will be cleared.")
# Call the function to clear the terminal
clear_terminal()
print("The terminal has been cleared, and this is new text.")

print(f"your name is {name}")