import csv

class MatchTestIO:
    FILE_PATH = "main/IO/csv/matchIO.csv"

    def read_file(self):
        with open(self.FILE_PATH, 'r', newline='',encoding="utf-8") as csvfile:
            return list(csv.reader(csvfile))