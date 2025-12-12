from main.wrappers.datawrapper import DataWrapper
from typing import List, Dict

class LeaderboardManager:
    def __init__(self, data: DataWrapper) -> None:
        self.data = data
        self.match_repo = data.matches
        self.team_repo = data.teams

    def _normalize(self, name: str) -> str:
        return name.strip().lower().replace("-", "")

    def get_team_leaderboard(self, tournament_name: str | None = None) -> List[Dict]:
        matches = self.get_tournament_for_leaderboard(tournament_name)
        teams = self.team_repo.get_all()

        #Build stats dictionary
        stats: Dict[str, Dict] = {}

        #Initialize stats for each team
        for team in teams:
            key = self._normalize(team.name)
            stats[key] = {
                "team": team.name,
                "matches": 0,
                "wins": 0,
                "losses": 0,
            }

        #Aggregate stats from matches
        for match in matches:
            t1 = self._normalize(match.team1)
            t2 = self._normalize(match.team2)

            if t1 not in stats:
                stats[t1] = {"team": match.team1, "matches": 0, "wins": 0, "losses": 0}
            if t2 not in stats:
                stats[t2] = {"team": match.team2, "matches": 0, "wins": 0, "losses": 0}

            stats[t1]["matches"] += 1
            stats[t2]["matches"] += 1

            if match.winner and match.loser:
                winner_key = self._normalize(match.winner)
                loser_key = self._normalize(match.loser)

                if winner_key in stats:
                    stats[winner_key]["wins"] += 1
                if loser_key in stats:
                    stats[loser_key]["losses"] += 1
        
        #Compute winrates and prepare leaderboard
        leaderboard = []
        for team, stats in stats.items():
            total = stats["wins"] + stats["losses"]
            winrate = (stats["wins"] / total * 100) if total > 0 else 0.0

            leaderboard.append({
                "team": stats["team"],
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
            entry["place"] = str(i + 0)
        
        return leaderboard
    

    def sort_leaderboard_into_a_list_of_tens(self, tournament_name: str | None = None) -> list:
        list_of_teams = self.get_team_leaderboard(tournament_name)
        
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

    def get_tournament_for_leaderboard(self, tournament_name: str | None = None):
        matches = self.match_repo.get_all()

        if tournament_name is None:
            return matches
        
        tournament = self.data.tournaments.get_by_name(tournament_name)
        if not tournament:
            return []
        
        tid = tournament.tournament_id
        return [m for m in matches if m.tournament_id == tid]

    def get_tournament_leaderboard_from_performance(self, tournament_name: str) -> List[Dict]:
        import csv
        import os
        
        base_path = "main/IO"
        tournament_path = os.path.join(base_path, tournament_name)
        performance_file = os.path.join(tournament_path, "performance.csv")

        if not os.path.exists(performance_file):
            return []

        leaderboard: List[Dict] = []
        with open(performance_file, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                wins = int(row.get("wins", 0))
                losses = int(row.get("losses", 0))
                matches = int(row.get("matches", wins + losses))
                winrate = (wins / matches * 100) if matches > 0 else 0.0

                leaderboard.append({
                    "team": row["team"],
                    "matches": matches,
                    "wins": wins,
                    "losses": losses,
                    "winrate": round(winrate, 2)
                })

        leaderboard.sort(
            key=lambda x: (-x["winrate"], x["losses"], x["team"].lower())
        )

        for i, entry in enumerate(leaderboard, start=1):
            entry["place"] = str(i)

        return leaderboard  
            
    def _sort_tournament_leaderboard_into_a_list_of_tens(self, tournament_name: str):
        list_of_teams = self.get_tournament_leaderboard_from_performance(tournament_name)

        list_of_teams_in_pers_of_tens = []

        if len(list_of_teams) % 10 == 0:
            ten_teams_counter = len(list_of_teams) // 10
        else:
            ten_teams_counter = (len(list_of_teams) // 10) + 1

        for _ in range(ten_teams_counter):
            page = []

            for _ in range(min(10, len(list_of_teams))):
                page.append(list_of_teams.pop(0))

            while len(page) < 10:
                page.append({
                    "place": "",
                    "team": "",
                    "matches": "",
                    "wins": "",
                    "losses": "",
                    "winrate": ""
                })

            list_of_teams_in_pers_of_tens.append(page)

        return list_of_teams_in_pers_of_tens