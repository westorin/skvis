from main.logic.tournamentmanager import TournamentManager

'''
To run the main UI type this into terminal: 

python3 -m main.UI.addtournament
'''
class AddTournamentUI:
    def __init__(self) -> None:
        self.tm = TournamentManager()

    def add_tournament_ui(self) -> None:
        print("=== Create new tournament ===")

        name = input("Name: ")
        start = input("Start date (DD-MM-YYYY): ")
        end = input("End date (DD-MM-YYYY): ")
        location = input("Location: ")
        contact_email = input("Contact email: ")
        contact_phone = input("Contact phone: ")

        data = {
            "name": name,
            "start": start,
            "end": end,
            "location": location,
            "contact_email": contact_email,
            "contact_phone": contact_phone,
        }

        try:
            self.tm.create_tournament(data)
            print("Tournament successfully created!")
        except ValueError as e:
            print("Error:", e)
        
# Temporary for testing
if __name__ == "__main__":
    ui = AddTournamentUI()
    ui.add_tournament_ui()
