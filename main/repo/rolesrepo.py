from main.IO.IOpy.roleIO import RoleIO
from main.models.rolemodel import Role

class RoleRepository:
    def __init__(self):
        self.io = RoleIO()
        self.roles = self.load_roles()

    def load_roles(self):
        rows = self.io.read_file()
        roles = []
        for row in rows:
            if row[0] == 'username':
                continue  # Skip header row
            else:
                username = row[0]
                role = row[1]

                r = Role(username, role)
                roles.append(r)

        return roles
    
    def get_role_by_username(self, username:str):
        print("Debug", [repr(role.username) for role in self.roles], repr(username))
        for role in self.roles:
            if role.username == username:
                return role
        return None
    
    def save_roles(self):
        rows = [["username", "role"]]
        for r in self.roles:
            rows.append([
                r.username,
                r.role
            ])
        self.io.write_file(rows)