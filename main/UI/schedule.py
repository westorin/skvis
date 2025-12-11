from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper


class ScheduleUI():
    def __init__(self) -> None:
        self.data = DataWrapper()
        self.logic = LogicWrapper(self.data)

    def print_schedule(self, tournament_name: str):
        pages = self.logic.tournament_manager.get_schedule_pages(tournament_name)
        return pages