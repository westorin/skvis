from typing import List, Dict

class TeamRepository:
    def __init__(self) -> None:
        self.io = TeamIO()
        self._teams: List[Dict] = self.