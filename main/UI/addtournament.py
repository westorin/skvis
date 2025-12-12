from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

'''
To run the main UI type this into terminal: 

python3 -m main.UI.addtournament
'''
class AddTournamentUI:
    def __init__(self, logic):
        self.logic = logic
        data = DataWrapper()
        logic = LogicWrapper(data)
        self.tm = logic.tournament_manager

    def add_tournament_ui(self) -> None:
        print("=== Create new tournament ===")
        
        event = ("CS") # input("Event: ")
        tournament_type = "Knockout"
        name = input("Name: ")
        start = input("Start date (DD-MM-YYYY): ")
        end = input("End date (DD-MM-YYYY): ")
        location = input("Location: ")
        contact_email = input("Contact email: ")
        contact_phone = input("Contact phone: ")
        points = "17" # Hvernig viljum við hafa þetta?

        data = {
            "event": event,
            "tournament_type": tournament_type,
            "name": name,
            "start": start,
            "end": end,
            "location": location,
            "contact_email": contact_email,
            "contact_phone": contact_phone,
            "points": points,
        }

        try:
            self.tm.create_tournament(data)
            print("Tournament successfully created!")
            input(">>>> ")
            return "BACK"
        except ValueError as e:
            print("Error:", e)
        
        
# Temporary for testing
if __name__ == "__main__":
    ui = AddTournamentUI()
    ui.add_tournament_ui()
