from main.repo.teamrepo import TeamRepository

lists = TeamRepository()
lists.load_teams()

print(lists.load_teams())