from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

data = DataWrapper()
logic = LogicWrapper(data)

#1 pick tournament
tournaments = logic.tournament_manager.list_tournaments()
eligible_tournaments = [
    t for t in tournaments
    if hasattr(t, 'teams') and len(t.teams) == 16
]
print("=== tournaments with 16 teams ===")
if not eligible_tournaments:
    print("No tournaments with exactly 16 teams found.")
    exit()

for idx, t in enumerate(eligible_tournaments, 1):
    print(f"{idx}. {t.name} ({len(t.teams)} teams)")

choice = input("Select a tournament by number: ").strip()
if not choice.isdigit() or not (1 <= int(choice) <= len(eligible_tournaments)):
    print("Invalid selection.")
    exit()

tournament = eligible_tournaments[int(choice) - 1]
tid = tournament.tournament_id
tname = tournament.name

print(f"Simulating tournament: {tname}")

#Helper: get all matches for this tournament
#TournamentManager
def get_matches_for_tournament(tournament_id):
    return [
        m for m in logic.match_manager.repo.get_all()
        if str(m.tournament_id) == str(tournament_id)
    ]

#Helper: get all WB matches for this tournament and round
#TournamentManager
def get_wb_round_matches(tournament_id, round_number: int):
    all_matches = logic.match_manager.repo.get_all()
    return [
        m for m in all_matches
        if str(m.tournament_id) == str(tournament_id)
        and m.bracket == "WB"
        and str(m.round) == round_number
    ]

#Helper: simulate all matches that have no winner yet
#MatchMangaer
def simulate_open_matches(stage_label: str):
    matches = get_matches_for_tournament(tid)
    open_matches = [m for m in matches if m.winner is None]

    if not open_matches:
        print(f"{stage_label}: All matches already simulated.")
        return
    
    print(f"\n{stage_label}: simulating {len(open_matches)} matches...")
    for m in open_matches:
        print(f"Simulating match {m.match_id}: {m.team1} vs {m.team2}")
        logic.match_manager.play_match_random(m.match_id)
    logic.match_manager.repo.save_to_file()
        

#2 Ensure WB Round 1 matches exist
matches = get_matches_for_tournament(tournament.tournament_id)
if not matches:
    print("No matches found for this tournament. Generating initial matches...")
    logic.tournament_manager.generate_initial_matches(tname)
    logic.match_manager.repo.save_to_file()
else:
    print(f"Found {len(matches)} existing matches for this tournament.")

#3 Simulate WB Round 1
simulate_open_matches("WB Round 1")

#4 Generate WB Round 2 matches and LB Round 1 matches
print("\nGenerating WB Round 2 and LB Round 1 matches...")
existing_wb_r2 = get_wb_round_matches(tid, 2)
if not existing_wb_r2:
    print("\nGenerating WB Round 2 matches...")
    logic.tournament_manager.generate_next_rounds(tname)
    logic.match_manager.repo.save_to_file()
else:
    print("WB Round 2 matches already exist.")

#5 Simulate WB round2 matches and LB round1 matches
simulate_open_matches("WB Round 2 and LB Round 1")

#6 Generate WB Round 3 semifinals from WB Round 2 winners
wb_r2 = get_wb_round_matches(tid, 2)
if len(wb_r2) != 4:
    print("Not enough WB R2 matches to generate WB R3 semifinals.")
    exit()

wb_r2 = sorted(wb_r2, key=lambda m: m.match_id)
wb2_winners = [m.winner for m in wb_r2]

wb3_pairs = [
    (wb2_winners[0], wb2_winners[1]),
    (wb2_winners[2], wb2_winners[3]),
]
print("\nGenerating WB Round 3 semifinals...")
for team1, team2 in wb3_pairs:
    match_data = logic.match_manager.create_tournament_match(
        team1 = team1, 
        team2 = team2,
        bracket = "WB",
        round_number = 3,
        tournament_id = tournament.tournament_id
    )
    #Immediatly simulate the match
    logic.match_manager.play_match_random(match_data.match_id)

logic.match_manager.repo.save_to_file()

#7 Generate WB Final from WB R3 winners
wb_r3 = get_wb_round_matches(tid, 3)
if len(wb_r3) != 2:
    print("Not enough WB R3 matches to generate WB Final.")
    exit()

wb_r3 = sorted(wb_r3, key=lambda m: m.match_id)
wb3_winners = [m.winner for m in wb_r3]

print("\nGenerating WB Final...")
final_match_data = logic.match_manager.create_tournament_match(
    team1 = wb3_winners[0],
    team2 = wb3_winners[1],
    bracket = "WB",
    round_number = 4,
    tournament_id = tournament.tournament_id
)
#Immediatly simulate the match
logic.match_manager.play_match_random(final_match_data.match_id)
logic.match_manager.repo.save_to_file()

#8 Determine and print the champion
final_match = logic.match_manager.repo.get_by_match_id(final_match_data.match_id)
champion = final_match.winner
runner_up = final_match.loser
print(f"\n=== Tournament Champion: {champion} ===")
print(f"Runner-up: {runner_up}")
print(f"Final Score: {final_match.final_score}")
print(f"Total Rounds Played: {final_match.total_rounds}")


print("Tournament simulation complete.")
print("You now have WB R2 and LB R1 matches simulated.")
print("We can extend this same pattern for further rounds")
