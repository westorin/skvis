from main.wrappers.datawrapper import DataWrapper

class TeamLogic():
    def __init__(self, data_wrapper: DataWrapper):
        self.data_wrapper = DataWrapper()

    def create_list_of_team_info_for_all(self, team_name: str):

        team = self.data_wrapper.teams.get_team(team_name)

        