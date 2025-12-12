from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper


class EnterMatchResultUI:
    def __init__(self, logic) -> None:
        self.logic = logic
        self.tm = self.logic.tournament_manager
        self.mm = self.logic.match_manager

    def run(self) -> None:
        print("=== Enter match result ===")

        tournaments = self.tm.list_tournaments()
        if not tournaments:
            print("No tournaments available.")
            return

        # Pick tournament
        print("\nAvailable tournaments:")
        for i, t in enumerate(tournaments, start=1):
            print(f"{i}. {t.name} ({len(t.teams)} teams)")

        choice = input("Select tournament (number, or q to quit): ").strip()
        if choice.lower() == "q":
            return

        try:
            t_index = int(choice) - 1
            tournament = tournaments[t_index]
        except (ValueError, IndexError):
            print("Invalid tournament selection.")
            return

        # List unplayed matches for that tournament
        matches = self.mm.repo.get_by_tournament(tournament.tournament_id)
        unplayed = [m for m in matches if m.winner is None]

        if not unplayed:
            print(f"No unplayed matches in tournament '{tournament.name}'.")
            return

        print(f"\nUnplayed matches in {tournament.name}:")
        for i, m in enumerate(unplayed, start=1):
            round_str = f"R{m.round}" if m.round is not None else ""
            bracket_str = m.bracket or ""
            print(
                f"{i}. [{bracket_str} {round_str}] "
                f"{m.team1} vs {m.team2} (match_id={m.match_id})"
            )

        choice = input("Select match (number, or q to cancel): ").strip()
        if choice.lower() == "q":
            return

        try:
            m_index = int(choice) - 1
            match = unplayed[m_index]
        except (ValueError, IndexError):
            print("Invalid match selection.")
            return

        # Enter final score
        print(f"\nEntering result for {match.team1} vs {match.team2}")
        score_str = input("Enter final score as 'X-Y' (no draws): ").strip()

        try:
            s1_str, s2_str = score_str.split("-")
            s1 = int(s1_str)
            s2 = int(s2_str)
        except Exception:
            print("Invalid score format. Use e.g. 13-11.")
            return

        # Call logic
        try:
            self.mm.play_match_manual(match.match_id, s1, s2)
        except ValueError as e:
            print(f"Error: {e}")
            return

        print("Result saved successfully.")


if __name__ == "__main__":
    ui = EnterMatchResultUI()
    ui.run()
