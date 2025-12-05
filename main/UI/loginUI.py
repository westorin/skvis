from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

class LoginUI:
    def __init__(self):
        data = DataWrapper()
        logic = LogicWrapper(data)
        self.login_manager = logic.login_manager
        
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