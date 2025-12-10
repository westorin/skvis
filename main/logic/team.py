from main.wrappers.datawrapper import DataWrapper

class TeamLogic():
    def __init__(self, data_wrapper: DataWrapper):
        self.data_wrapper = DataWrapper()

    def create_list_of_team_info_for_all(self, team_name: str):

        team = self.data_wrapper.teams.get_team(team_name)
        
        list_of_all_team_info = []

        team_list = [team.name, team.captain, team.website_url]
        list_of_all_team_info.append(team_list)
        for player in team.players:
            list_of_player_info = []
            player_info = self.data_wrapper.players.get_by_handle(player)
            if(len(player_info.name) > 20):
                list_of_player_info.append(player_info.name[0:17] + "...")
            else:
                list_of_player_info.append(player_info.name)

            if(len(player_info.username) > 20):
                list_of_player_info.append(player_info.username[0:17] + "...")
            else:
                list_of_player_info.append(player_info.username)

            list_of_all_team_info.append(list_of_player_info)

        for i in range(0, (5 - len(team.players))):
            list_of_player_info = ["", ""]

            list_of_all_team_info.append(list_of_player_info)
        
    

        return list_of_all_team_info