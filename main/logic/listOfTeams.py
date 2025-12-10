from main.repo.teamrepo import TeamRepository

class ListOfTeamsLogic():
    def __init__(self):
        self.team_repo = TeamRepository()

    def get_all_teams(self):
        return self.team_repo.teams
    
    
    def print_list_of_teams(self):
        teams = ListOfTeamsLogic().get_all_teams()

        for team in teams:
            print("Team:", team.name)
            print("Captain:", team.captain)
            print("Players:", ", ".join(team.players))
            print("Website:", team.website_url)
            print("-----")

        print(teams[0].name)
        print(len(teams) % 10)
        # ^^^ má ekki :(


    def make_list_of_all_teams(self) -> list:
        all_teams_data = ListOfTeamsLogic().get_all_teams()

        list_of_teams = []
        
        # Here we take one team at a time and we put it all the data of the team in to a list that we then put it in another list
        for team in all_teams_data:
            list_of_one_team = []
            if(len(team.name) > 20):
                list_of_one_team.append(team.name[0:16] + "...")
            else:
                list_of_one_team.append(team.name)

            if(len(team.captain) > 20):
                list_of_one_team.append(team.captain[0:16] + "...")
            else:
                list_of_one_team.append(team.captain)

            if(len(team.website_url) > 20):
                list_of_one_team.append(team.website_url[0:16] + "...")
            else:
                list_of_one_team.append(team.website_url)

            list_of_teams.append(list_of_one_team)
        
        return list_of_teams
            

    def sort_teams_into_a_list_of_tens(self) -> list:
        list_of_teams = ListOfTeamsLogic().make_list_of_all_teams()
        
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
                    list_of_teams = list_of_teams[1:]

                for i in range(0, (10 - (len(list_of_teams) % 10))):
                    lists_of_ten_teams.append(["", "", ""])
                list_of_teams_in_pers_of_tens.append(lists_of_ten_teams)
                list_of_teams = []

        return list_of_teams_in_pers_of_tens