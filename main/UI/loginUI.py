from main.logic.loginmanager import LoginManager
from main.repo.playerrepo import PlayerRepository
from main.repo.rolesrepo import RoleRepository
from main.repo.passwordrepo import PasswordRepository

class LoginUI:
    def __init__(self):
        self.login_manager = LoginManager(PlayerRepository(), RoleRepository(), PasswordRepository())

    def login(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        role = self.login_manager.authenticate(username, password)
        if role:
            print(f"Login successful! Role: {role}")
            return role
        else:
            print("Invalid username or password.")
            return None

if __name__ == "__main__":
    LoginUI().login()