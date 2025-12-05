from main.logic.matchmanager import MatchManager


class MatchUI:
    def __init__(self) -> None:
        self.mm = MatchManager()

    def create_match_ui(self):
        print("=== Create match ===")
        date = input("Date (DD-MM-YYYY): ")
        time = input("Time (HH:MM): ")
        server_id = input("Server ID: ")
        team1 = input("Team 1: ")
        team2 = input("Team 2: ")
        round_name = input("Round (optional): ")
        tournament = input("Tournament: ")

        data = {
            "date": date,
            "time": time,
            "server_id": server_id,
            "team1": team1,
            "team2": team2,
            "round": round_name or None,
            "tournament": tournament or None,
        }

        try:
            match = self.mm.create_match(data)
            print(f"Match saved: {match.team1} vs {match.team2} on server {match.server_id}")
        except ValueError as e:
            print("Error:", e)

    def list_matches_ui(self):
        matches = self.mm.list_matches()
        if not matches:
            print("No matches recorded.")
            return

        print("=== Matches ===")
        for m in matches:
            score = f"{m.score1}-{m.score2}"
            winner = f" | winner: {m.winner}" if m.winner else ""
            print(f"{m.date} {m.time} | {m.team1} vs {m.team2} | score {score}{winner} | server {m.server_id}")


if __name__ == "__main__":
    ui = MatchUI()
    while True:
        print("\n1. Create match\n2. List matches\nq. Quit")
        choice = input("Choose: ").strip().lower()
        if choice == "1":
            ui.create_match_ui()
        elif choice == "2":
            ui.list_matches_ui()
        elif choice == "q":
            break
        else:
            print("Invalid choice.")
