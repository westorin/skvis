import main.models.passwordsmodel as PasswordsModel
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from main.repo.playerrepo import PlayerRepository
    from main.repo.rolesrepo import RoleRepository
    from main.repo.passwordrepo import PasswordRepository

class LoginManager:
    """Handles user authentication and role resolution."""

    def __init__(self, player_repo: "PlayerRepository", role_repo: "RoleRepository", password_repo: "PasswordRepository") -> None:
        """Initialize the login manager with required repositories."""
        self.player_repo = player_repo
        self.role_repo = role_repo
        self.password_repo = password_repo

    def authenticate(self, username, password):
        """Authenticate a user and return their role if successful."""
        username = username.strip()
        password = password.strip()

        # Look up stored password entry
        entry = self.password_repo.get_by_username(username)
        if entry is None:
            return None
        
        # Compare passwords
        if entry.password.strip() != password:
            return None
        
        # Look up user role
        role_entry = self.role_repo.get_role_by_username(username)
        if role_entry:
            return role_entry.role
        
        # Default role if no specific role is found
        return "player"