from main.logic.leaderboardmanager import LeaderboardManager
from main.wrappers.datawrapper import DataWrapper
from main.logic.listOfPlayers import ListOfPlayersLogic
from main.logic.clearScreenInTerminal import clear_screen


class TeamLeaderBoardUI():
     def __init__(self):
         pass
     
     def print_team_leader_board(self):
         
          data = DataWrapper()
          leaderboard_manager = LeaderboardManager(data)

          teams = leaderboard_manager.get_team_leaderboard()

          page = leaderboard_manager.sort_leaderboard_into_a_list_of_tens()

          header_text = """+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t+---------------------------------------------------+\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t| ╔╦╗┌─┐┌─┐┌┬┐  ╦  ┌─┐┌─┐┌┬┐┌─┐┬─┐  ╔╗ ┌─┐┌─┐┬─┐┌┬┐ |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t|  ║ ├┤ ├─┤│││  ║  ├┤ ├─┤ ││├┤ ├┬┘  ╠╩╗│ │├─┤├┬┘ ││ |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t|  ╩ └─┘┴ ┴┴ ┴  ╩═╝└─┘┴ ┴─┴┘└─┘┴└─  ╚═╝└─┘┴ ┴┴└──┴┘ |\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t+---------------------------------------------------+\t\t\t\t\t\t\t\t|"""

          top_leader_board = f"""
+------+----------------------+-----------+-----------+-----------+------------+
| Nr.  | Team name            | Matches   | wins      | Losses    | Win rate % |
+======+======================+===========+===========+===========+============+

"""

          print(header_text)
          i = input()

# print("=== Team Leaderboard ===")
# while True:
#     display_teams = page[current]
#     print(f"Page {current + 1} of {len(page)}")
#     for team in display_teams:
#         print(f"Place: {team['place']}, Team: {team['team']}, Matches: {team['matches']}, Wins: {team['wins']}, Losses: {team['losses']}, Winrate: {team['winrate']}%")
#     print("\n====")
#     print("d: Down Page | u: Up Page | q: Quit")

#     choice = input("Enter your choice: ").lower().strip()

#     if choice == "d":
#         if current < len(page) - 1:
#             current += 1
#         else:
#             print("You are already on the last page.")
#     elif choice == "u":
#         if current > 0:
#             current -= 1
#         else:
#             print("You are already on the first page.")
#     elif choice == "q":
#         break
#     else:
#         print("Invalid choice. Please enter 'd', 'u', or 'q'.")


# for team in teams:
#     print(f"Place: {team['place']}, Team: {team['team']}, Matches: {team['matches']}, Wins: {team['wins']}, Losses: {team['losses']}, Winrate: {team['winrate']}%")
# print(teams)
# print(teams[0]["team"])
# print(teams[0]["wins"])  # Example of accessing team name of the second team in the leaderboard

