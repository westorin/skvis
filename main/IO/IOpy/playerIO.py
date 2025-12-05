import csv

class PlayerIO:
    FILE_PATH = "main/IO/csv/playerIO.csv"

    def read_file(self):
        with open(self.FILE_PATH, 'r', newline='') as csvfile:
            return list(csv.reader(csvfile))
        
    def write_file(self, rows):
        with open(self.FILE_PATH, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(rows)