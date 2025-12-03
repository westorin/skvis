from typing import List, Dict
from main.IO.teamIO import TeamIO

class TeamRepository:
    def __init__(self) -> None:
        self.io = TeamIO()
        self._teams: List[Dict] = self.