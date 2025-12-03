from typing import List, Dict # Type hinting
from import

class TeamManager:
    """Handles creating and storing teams in memory."""

    def __init__(self) -> None:
        self.repo = TeamRepository()