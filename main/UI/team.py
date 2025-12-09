import math


class TeamUI():
    def __init__(self):
        pass

    def print_team(self, team_name: str) -> str:
        self.team_name = team_name
        
        team_capt_name = ""

        wins = ""
        losses = ""
        win_rate = ""

        header_text = f"""
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         +------------------------------------------+          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         | {" "*math.floor((40 -len(team_name))/2) + team_name + " "*math.ceil((40 -len(team_name))/2)} |          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t         +------------------------------------------+          \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t     +----------------------+--------+--------+----------+     \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t| Team Captain         |  Wins  | losses | Win rate | URL.|     \t\t\t\t\t\t\t\t|
|\t\t\t\t\t    +======================+========+========+==========+======================+\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t     | {team_capt_name + " "*(20 - len(team_capt_name))} | {wins + " "*(6 - len(wins))} | {losses + " "*(6 -len(losses))} | {win_rate + " "*(8 -len(win_rate))} |     \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t     +----------------------+--------+--------+----------+     \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        | Name                 | Username             |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +======================+======================+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        |                      |                      |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        |                      |                      |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        |                      |                      |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        |                      |                      |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        |                      |                      |        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t        +----------------------+----------------------+        \t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
"""
        

        print(header_text)



