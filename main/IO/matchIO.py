import csv
from typing import List

class MatchIO:
    FILE_PATH = ""main/IO/MatchIO.csv""

    def read_file(self) -> List[list[str]]:
        with open(self.FILE_PATH, "r", newline="") as csvfile:
            return list(csv.reader(csvfile))
        
    def write_file(self, rows: List[list[str]]) -> None:
        with open(self.FILE_PATH, "w", newline="") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(rows)