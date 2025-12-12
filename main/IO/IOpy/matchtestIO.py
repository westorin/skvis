import csv

class MatchTestIO:
    FILE_PATH: str = "main/IO/csv/matchIO.csv"

    def read_file(self) -> list[list[str]]:
        with open(self.FILE_PATH, 'r', newline='',encoding="utf-8") as csvfile:
            return list(csv.reader(csvfile))