# IO/tournamentIO.py

import csv
from typing import List

class TournamentIO:
    FILE_PATH = "main/IO/csv/tournamentIO.csv"

    def read_file(self) -> List[list[str]]:
        with open(self.FILE_PATH, "r", newline="",encoding="utf-8") as csvfile:
            return list(csv.reader(csvfile))
        
    def write_file(self, rows: List[list[str]]) -> None:
        with open(self.FILE_PATH, "w", newline="", encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(rows)