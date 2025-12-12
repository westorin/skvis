
class InputMatchResultsUI():
    def __init__(self):
        pass

    def print_input_match_resutls(self, tournament_name: str):
        
        name_of_tournament = ""

        name_of_team_a = ""
        name_of_team_b = ""

        score_a = ""
        score_b = ""

        header_text = f""" 
+------------------------------------------+
| {name_of_tournament} |
+------------------------------------------+

+----------------------+-------+
| Name of team         | Score |
+======================+=======+
| {name_of_team_a} | {score_a} |
+----------------------+-------+
| {name_of_team_b} | {score_b} |
+----------------------+-------+
"""

        print(header_text)