import main.models.passwordsmodel as PasswordsModel

class LoginManager:
    def __init__(self, player_repo, role_repo, password_repo):
        self.player_repo = player_repo
        self.role_repo = role_repo
        self.password_repo = password_repo

    # Authenticate user and return role if successful
    def authenticate(self, username, password):
        username = username.strip()
        password = password.strip()

        # Get password entry
        entry = self.password_repo.get_by_username(username)
        if entry is None:
            return None
        
        # Check password
        if entry.password.strip() != password:
            return None
        
        # Get role entry
        role_entry = self.role_repo.get_role_by_username(username)
        if role_entry:
            return role_entry.role
        
        # Default role if none found
        return "player"