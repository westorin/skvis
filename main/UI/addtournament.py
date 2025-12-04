from main.logic.tournamentmanager import TournamentManager

'''
To run the main UI type this into terminal: 

python3 -m main.UI.addtournament (virkar ekki)
'''
class AddTournamentUI:
    def __init__(self) -> None:
        self.tm = TournamentManager()

    def add_tournament_ui(self) -> None:
        print("=== Create new tournament ===")

        name = input("Name: ")
        start_date = input("Start date (YYYY-MM-DD): ")
        end_date = input("End date (YYYY-MM-DD): ")
        location = input("Location: ")
        contact_email = input("Contact email: ")
        contact_phone = input("Contact phone: ")

        data = {
            "name": name,
            "start_date": start_date,
            "end_date": end_date,
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
