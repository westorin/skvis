import main.repo.playerrepo as PlayerRepository
import main.repo.passwordrepo as PasswordRepository

class LoginManager:
    def __init__(self, player_repo, role_repo, password_repo):
        self.player_repo = player_repo
        self.role_repo = role_repo
        self.password_repo = password_repo

    def authenticate(self, username, password):
        username = username.strip()
        password = password.strip()

        entry = self.password_repo.get_by_username(username)
        if entry is None:
            return None
        
        if entry.password.strip() != password:
            return None
        
        return entry.username  # Return username on successful authentication