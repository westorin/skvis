from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

data = DataWrapper()
logic = LogicWrapper(data)

tournaments = logic.tournament_manager.list_tournaments()
eligible_tournaments = [
    t for t in tournaments
    if hasattr(t, 'teams') and len(t.teams) == 16
]

print("=== Available Tournaments for Match Simulation(16 teams) ===")
if not eligible_tournaments:
    print("No tournaments with exactly 16 teams found.")
    exit()

for idx, t in enumerate(eligible_tournaments, 1):
    print(f"{idx}. {t.name} ({len(t.teams)} teams)")

choice = input("Select a tournament by number: ").strip()

if not choice.isdigit() or not (1 <= int(choice) <= len(eligible_tournaments)):
    print("Invalid selection.")
    exit()

selected_tournament = eligible_tournaments[int(choice) - 1]
print(f"You selected: {selected_tournament.name}")
existing_matches = [
    m for m in logic.match_manager.repo.get_all()
    if str(m.tournament_id) == str(selected_tournament.tournament_id)
]
if not existing_matches:
    print("No matches found for this tournament. Generating initial matches...")
    logic.tournament_manager.generate_initial_matches(selected_tournament.name)
    existing_matches = logic.match_manager.repo.get_by_tournament(selected_tournament.tournament_id)
else:
    print(f"Found {len(existing_matches)} existing matches for this tournament.")

matches = [
    m for m in logic.match_manager.repo.get_all()
    if str(m.tournament_id) == str(selected_tournament.tournament_id)
]

if not matches:
    print("No matches found for this tournament.")

print(f"Simulating {len(matches)} matches for tournament '{selected_tournament.name}'...")

for match in matches:
    print(f"Simulating match {match.match_id}: {match.team1} vs {match.team2}")
    logic.match_manager.play_match_random(match.match_id)
    updated_match = logic.match_manager.repo.get_by_match_id(match.match_id)

    print("Winner",updated_match.winner)
    print("Loser",updated_match.loser)
    print("Final Score",updated_match.final_score)
    print("Total Rounds Played",updated_match.total_rounds)
    print("-----")

logic.match_manager.repo.save_to_file()
print("All matches simulated and saved successfully.")
print("=== Simulation Complete ===")