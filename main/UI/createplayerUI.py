#UI → PlayerManager → PlayerRepository → PlayerIO → CSV

'''
Viljum við þegar við búum til nýjan player að hann fær að velja lið eða viljum við að fær að búa til lið?
hvernig þetta er núna er að hann býr til lið sem er eingöngu í playerIO.csv og ekkert gerist í teamIO.csv
Kannski bæta við að liðið sé ekki til og lista öll liðin sem hann getur farið í?
Eða láta hann fá að búa til lið og liðið er bara tómt nema nafnið á liðinu?
'''

from main.logic.playermanager import PlayerManager
from main.logic.teammanager import TeamManager

class PlayerUI:
    def __init__(self):
        self.pm = PlayerManager()
        self.tm = TeamManager()

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
        except ValueError as e:
            print("\nError:", e)

if __name__ == "__main__":
    PlayerUI().register_player_ui()

#        def register_player_is_empty(self, name, dob, address, phone, email, url, username, team):
#           return not all([name, dob, address, phone, email, url, username, team])