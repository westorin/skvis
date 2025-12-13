#UI → PlayerManager → PlayerRepository → PlayerIO → CSV
#Wrappers = UI → LogicWrapper → (Logic Managers) → DataWrapper → (Repositories) → IO → CSV
'''
Viljum við þegar við búum til nýjan player að hann fær að velja lið eða viljum við að fær að búa til lið?
hvernig þetta er núna er að hann býr til lið sem er eingöngu í playerIO.csv og ekkert gerist í teamIO.csv
Kannski bæta við að liðið sé ekki til og lista öll liðin sem hann getur farið í?
Eða láta hann fá að búa til lið og liðið er bara tómt nema nafnið á liðinu?
'''

from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

class PlayerUI:
    def __init__(self):
        data = DataWrapper()
        logic = LogicWrapper(data)
        self.pm = logic.player_manager

    def register_player_ui(self):
#       if register_player_is_empty:
#            print("\nError: All fields are required.")
#            return
        
        print("=== Register New Player ===")

        name = input("Name: ")
        dob = input("DOB (DD-MM-YYYY): ")
        address = input("Address: ")
        phone = input("Phone: ")
        email = input("Email: ")
        url = input("URL: ")
        username = input("Username (handle): ")

        while True:
            team = input("Team (must exist): ").strip()
            if team == "":
                break

            from main.repo.teamrepo import TeamRepository
            tr = TeamRepository()

            if tr.get_team(team) is not None:
                break

            print("\nThat team does not exist.")
            print("Available teams:")
            for t in tr.teams:
                print(" -", t.name)
            print("Try again.\n")

        # TODO It registers player even if you enter nothing as an input
        try:
            player = self.pm.register_player(
                name, dob, address, phone, email, url, username, team
            )
            if team.strip():
                try:
                    self.tm.add_player_to_team(team, username)
                except Exception as e:
                    print("Warning: could not add player to team:", e)
            print("\nPlayer successfully registered!")
            return "BACK"
        except ValueError as e:
            print("\nError:", e)
        return "BACK"
#        def register_player_is_empty(self, name, dob, address, phone, email, url, username, team):
#           return not all([name, dob, address, phone, email, url, username, team])