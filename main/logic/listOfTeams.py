from main.repo.teamrepo import TeamRepository

class lists_of_teams():
    def __init__(self):
        pass

lists = TeamRepository()
lists.load_teams()

print(lists.load_teams())