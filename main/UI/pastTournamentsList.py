from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper
from main.logic.clearScreenInTerminal import clear_screen

class PastTournamentsUI():
    def __init__(self):
        pass

    def print_tournaments(self):
        data = DataWrapper()
        logic = LogicWrapper(data)
        self.tm = logic.tournament_manager
        print(self.tm.list_past_tournaments())