from typing import List, Optional

from main.IO.IOpy.passwordsIO import PasswordsIO
from main.models.passwordsmodel import PasswordsManager

class PasswordRepository:
    """Repository responsible for loading and accessing user passwords."""
    def __init__(self) -> None:
        self.io = PasswordsIO()
        self.passwords: List[PasswordsManager] = self.load_passwords()

    def load_passwords(self) -> List[PasswordsManager]:
        rows = self.io.read_file()
        passwords: List[PasswordsManager] = []

        for row in rows:
            if row[0] == 'username':
                continue  # Skip header row

            p = PasswordsManager(*row)
            passwords.append(p)

        return passwords

    def get_by_username(self, username: str) -> Optional[PasswordsManager]:
        """Retrieve a password entry by username."""
        username = username.strip()
        
        for p in self.passwords:
            if p.username == username:
                return p
        return None