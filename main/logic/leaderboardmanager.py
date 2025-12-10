from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper
from typing import List, Dict

class LeaderboardManager:
    def __init__(self, data: DataWrapper) -> None:
        self.data = data
        self.match_repo = data.matches
        self.team_repo = data.teams

    def get_team_leaderboard(self) -> List[Dict]:
        matches = self.match_repo.get_all()
        teams = self.team_repo.get_all()

        #Build stats dictionary
        stats: Dict[str, Dict] = {}

        #Initialize stats for each team
        for team in teams:
            stats[team.name] = {
                "team": team.name,
                "matches": 0,
                "wins": 0,
                "losses": 0,
            }

        #Aggregate stats from matches
        for match in matches:
            t1 = match.team1
            t2 = match.team2

            if t1 not in stats or t2 not in stats:
                continue  # Skip if team not found

            stats[t1]["matches"] += 1
            stats[t2]["matches"] += 1

            if match.winner and match.loser:
                if match.winner in stats:
                    stats[match.winner]["wins"] += 1
                if match.loser in stats:
                    stats[match.loser]["losses"] += 1
        
        #Compute winrates and prepare leaderboard
        leaderboard = []
        for team, stats in stats.items():
            total = stats["wins"] + stats["losses"]
            winrate = (stats["wins"] / total * 100) if total > 0 else 0.0

            leaderboard.append({
                "team": team,
                "matches": stats["matches"],
                "wins": stats["wins"],
                "losses": stats["losses"],
                "winrate": round(winrate, 2)
            })

        #Sort leaderboard by winrate descending
        leaderboard.sort(
            key=lambda x: (-x["winrate"], x["losses"], x["winrate"], x["team"].lower())
        )

        #Add place numbers
        for i, entry in enumerate(leaderboard, start=1):
            entry["place"] = i + 0
        
        return leaderboard
    

    def sort_leaderboard_into_a_list_of_tens(self) -> list:
        list_of_teams = self.get_team_leaderboard()
        
        list_of_teams_in_pers_of_tens = []
        
        if(len(list_of_teams) % 10 == 0):
            ten_teams_counter = (len(list_of_teams) // 10)
        else:
            ten_teams_counter = (len(list_of_teams) // 10)+ 1

        for t in range(0, ten_teams_counter):
            lists_of_ten_teams = []
            # Here we check if the list of the all teams has 10 teams to add
            if((len(list_of_teams) // 10 ) > 0):
                # Here we have a for loop that counts ten so we can add the ten teams to a list and remove the on you add
                for i in range(0,10):
                    lists_of_ten_teams.append(list_of_teams[0])
                    list_of_teams = list_of_teams[1:]                
                    
                list_of_teams_in_pers_of_tens.append(lists_of_ten_teams)
    
            # Here we check if the list of all teams has less then 10 teams
            elif((len(list_of_teams) // 10 ) == 0 and (len(list_of_teams) % 10) != 0):
                for team in list_of_teams:
                    lists_of_ten_teams.append(team)
                    
                remaining_slots = len(list_of_teams)
                blank_slots = 10 - remaining_slots

                for i in range(blank_slots):
                    lists_of_ten_teams.append({
                        "place": "",
                        "team": "",
                        "matches": "",
                        "wins": "",
                        "losses": "",
                        "winrate": ""
                    })
                
                list_of_teams_in_pers_of_tens.append(lists_of_ten_teams)
                list_of_teams = []

        return list_of_teams_in_pers_of_tens
