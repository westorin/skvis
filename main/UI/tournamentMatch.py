


class TournamentMatchsUI():
    def __init__(self, logic):
        self.logic = logic


    def print_matchs(self, tournament_name: str) -> str:
        print("lol")

        self.logic.clear_screen.clear()

        matches = self.logic.match_manager.get_matches_for_tournament_by_name(tournament_name)


        header_text = f"""        
+----------+----------------------+-----+----------------------+-------+----------------------+
| Game Nr. | Red Team             | Vs. | Blue Team            | score | Winner               | 
+==========+======================+=====+======================+=======+======================+"""
        print(header_text)

        if not matches:
            print("No matches found for this tournament.")
            return "BACK"
        else:
            for match in matches:
                game_nr = str(match.match_id).ljust(8)
                team1 = match.team1.ljust(20)
                team2 = match.team2.ljust(20)
                score = (match.final_score or "-").ljust(5)
                winner = (match.winner or "-").ljust(20)

                print(f"| {game_nr} | {team1} | Vs. | {team2} | {score} | {winner} |")
                print("+----------+----------------------+-----+----------------------+-------+----------------------+")

        choice = str(input(">>>> "))

        if(choice.lower() == "q"):
            return "QUIT"
        elif(choice.lower() == "b"):
            return "BACK"