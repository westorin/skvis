from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

class AddTeamsToTournamentUI:
    def __init__(self,logic):
        self.logic = logic
    def add_teams_ui(self):
        print("=== Add Teams to Tournament ===")

        tournaments = self.logic.tournament_manager.list_tournaments()
        if not tournaments:
            print("No tournaments available. Please create a tournament first.")
            return
        
        print("Available Tournaments:")
        for t in tournaments:
            print(" -", t.name)

        tournament_name = input("Enter Tournament name: ").strip()
        tournament = self.logic.tournament_manager.get_tournament(tournament_name)
        if tournament is None:
            print(f"Tournament '{tournament_name}' does not exist.")
            return
        print("Available Teams:")
        teams = self.logic.team_manager.get_all_teams()
        for team in teams:
            print(" -", team.name)
        
        selected = []
        while len(selected) < 16:
            team_name = input("Enter Team name to add (or press Enter to finish): ").strip()
            if team_name == "":
                break
            if team_name in selected:
                print("Team already selected.")
                continue
            team = self.logic.team_manager.get_team(team_name)
            if team is None:
                print(f"Team '{team_name}' does not exist.")
                continue
            selected.append(team_name)
            print(f"Team '{team_name}' selected.")
            print("List of all team")

        if len(selected) != 16:
            print("You must select exactly 16 teams to proceed.")
            return

        try:
            self.logic.tournament_manager.set_teams_for_tournament(tournament_name, selected)
            print(f"Teams added to tournament '{tournament_name}' successfully.")
        except Exception as e:
            print("Error:", e)