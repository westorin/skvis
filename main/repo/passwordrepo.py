from main.IO.passwordsIO import PasswordsIO
from main.models.passwordsmodel import PasswordsManager

class PasswordRepository:
    def __init__(self):
        self.io = PasswordsIO()
        self.passwords = self.load_passwords()


    def load_passwords(self):
        rows = self.io.read_file()
        passwords = []

        for row in rows:
            if row[0] == 'username':
                continue  # Skip header row
            else:
                p = PasswordsManager(*row)
                passwords.append(p)

        return passwords

    # Get password by username
    def get_by_username(self, username: str):
        username = username.strip()
        
        for p in self.passwords:
            if p.username == username:
                return p
        return None
    
    
    