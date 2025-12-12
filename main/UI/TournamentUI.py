from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

class TournamentUI():
    def tournament_has_matches(tournament):
        data = DataWrapper()
        logic = LogicWrapper(data)
        return len(logic.match_manager.repo.get_by_tournament(tournament.tournament_id)) > 0

    def run_tournament_ui(self):
        data = DataWrapper()
        logic = LogicWrapper(data)
        
        tournaments = data.tournaments.get_all()
        print("=== Available Tournaments ===")

        for i, t in enumerate(tournaments, start=1):
            print(f"{i}. {t.name} ({len(t.teams)} teams)")

        choice = int(input("Select a tournament by number: ").strip()) - 1
        selected_tournament = tournaments[choice]
        tname = selected_tournament.name

        print(f"\nChoose tournament execution mode")
        print("1. Full Automatic Simulation")
        print("2. Manual")
        mode = input("Select mode (1 or 2): ").strip()

        if mode == "1":
            execution_mode = "automatic"
        elif mode == "2":
            execution_mode = "manual"
        else:
            print("Invalid mode selected.")
            exit()


        print("\nChoose tournament format")
        print("1. Double Elimination")
        print("2. Single Elimination (Knockout)")
        fmt = input("Select tournament format:").strip()

        if mode == "1":
            if fmt == "1":
                result = logic.tournament_manager.run_full_simulation(selected_tournament)
            elif fmt == "2":
                result = logic.tournament_manager.run_single_elimination(selected_tournament)
            else:
                raise ValueError("Invalid format selected.")
        elif mode == "2":
            if fmt != "2":
                raise ValueError("Manual mode only supports Single Elimination format.")
            if self.tournament_has_matches(selected_tournament):
                print("\nThis tournament already has matches")
                print("Manual mode requires a fresh tournament")
                print("Please create a new tournament for manual mode")
                exit()
            result = logic.tournament_manager.run_single_elimination_manual(selected_tournament)
            while result["status"] == "awaiting_input":
                match = result["match"]
                print(f"\nMatch {match.match_id}: {match.team1} vs {match.team2}")
                score1 = int(input(f"Enter score for {match.team1}: ").strip())
                score2 = int(input(f"Enter score for {match.team2}: ").strip())
                logic.match_manager.set_match_result(match.match_id, score1, score2)
                result = logic.tournament_manager.run_single_elimination_manual(selected_tournament)
        else:
            raise ValueError("Invalid mode selected.")

        print("\n======== TOURNAMENT RESULTS ========")
        print(f"Tournament: {tname}")
        #Manual mode
        if isinstance(result, dict) and result.get("status") == "completed":
            summary = result["summary"]
        #Automatic mode
        elif isinstance(result, dict) and "champion" in result:
            summary = result
        else:
            raise ValueError("Tournament did not complete successfully.")

        print(f"Champion: {summary['champion']}")
        print(f"Runner-up: {summary['runner_up']}")
        print(f"Final Score: {summary['final_score']}")
        print(f"Total Rounds: {summary['total_rounds']}")

        return "BACK"
