from main.repo.teamrepo import TeamRepository

class ListOfTeamsLogic():
    def __init__(self):
        self.team_repo = TeamRepository()

    def get_all_teams(self):
        return self.team_repo.teams
    
    
    def print_list_of_teams(self):
        teams = ListOfTeamsLogic().get_all_teams()
        logic = ListOfTeamsLogic()

        for team in teams:
            print("Team:", team.name)
            print("Captain:", team.captain)
            print("Players:", ", ".join(team.players))
            print("Website:", team.website_url)
            print("-----")

        print(teams[0].name)
        print(len(teams))

if __name__ == "__main__":
    ListOfTeamsLogic().print_list_of_teams()