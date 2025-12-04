import csv

class PasswordsIO:
    FILE_PATH = "main/IO/passwords.csv"

    def read_file(self):
        with open(self.FILE_PATH, 'r', newline='') as csvfile:
            return list(csv.reader(csvfile))
        