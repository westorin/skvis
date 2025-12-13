from main.UI.addteamstotournamentUI import AddTeamsToTournamentUI
'''
To run the main UI type this into terminal: 

python3 -m main.UI.addtournament
'''
class AddTournamentUI:
    def __init__(self, logic):
        self.logic = logic
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
            print("Tournament successfully created!\n")

            tournaments = self.tm.get_all_tournaments()

            while True:
                choice = "1"
                if not choice.isdigit():
                    print("Please enter a number.")
                    continue

                choice = int(choice) - 1
                if 0 <= choice < len(tournaments):
                    selected_tournament = tournaments[choice]
                    break
                else:
                    print("Invalid selection.")

            add_teams_ui = AddTeamsToTournamentUI(self.logic)
            selected_teams = add_teams_ui.add_teams_ui()

            if selected_teams:
                self.tm.set_teams_for_tournament(
                    selected_tournament.name,
                    selected_teams
                )
                print("Teams successfully added to the tournament!")

            return "BACK"
        except ValueError as e:
            print("Error:", e)
            input(">>>> ")
            return "BACK"
        return "BACK"
