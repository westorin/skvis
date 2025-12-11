from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

data = DataWrapper()
logic = LogicWrapper(data)

tournaments = data.tournaments.get_all()
print("=== Available Tournaments ===")

for i, t in enumerate(tournaments, start=1):
    print(f"{i}. {t.name} ({len(t.teams)} teams)")

choice = input("Select a tournament by number: ").strip()
choice = int(choice) - 1
selected_tournament = tournaments[choice]
tname = selected_tournament.name

print("\nChoose tournament format")
print("1. Double Elimination")
print("2. Single Elimination (Knockout)")
fmt = input("Select tournament format:")

if fmt == "1":
    result = logic.tournament_manager.run_full_simulation(selected_tournament)
elif fmt == "2":
    result = logic.tournament_manager.run_single_elimination(selected_tournament)
else:
    print("Invalid format selected.")
    exit()


champion = result["champion"]
runner_up = result["runner_up"]
final_score = result["final_score"]
total_rounds = result["total_rounds"]

print("\n======== TOURNAMENT RESULTS ========")
print(f"Tournament: {tname}")
print(f"Champion: {champion}")
print(f"Runner-Up: {runner_up}")
print(f"Final Score: {final_score}")
print(f"Total Rounds Played: {total_rounds}")
