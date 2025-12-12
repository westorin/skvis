from typing import List, Optional

from main.IO.IOpy.roleIO import RoleIO
from main.models.rolemodel import Role

class RoleRepository:
    """Repository responsible for loading, storing and retrieving user roles."""
    def __init__(self) -> None:
        self.io: RoleIO = RoleIO()
        self.roles: List[Role] = self.load_roles()

    def load_roles(self) -> List[Role]:
        """Load roles from CSV and convert them into Role objects."""
        rows = self.io.read_file()
        roles: List[Role] = []

        for row in rows:
            if row[0] == 'username':
                continue  # Skip header row

            username = row[0]
            role = row[1]

            r = Role(username, role)
            roles.append(r)

        return roles
    
    def get_role_by_username(self, username: str) -> Optional[Role]:
        """Retrieve the role entry for a given username."""
        for role in self.roles:
            if role.username == username:
                return role
        return None
    
    def save_roles(self) -> None:
        rows = [["username", "role"]]
        for r in self.roles:
            rows.append([
                r.username,
                r.role
            ])
        self.io.write_file(rows)