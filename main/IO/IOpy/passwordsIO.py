import csv

class PasswordsIO:
    """Handles reading raw password data from CSV."""

    FILE_PATH: str = "main/IO/csv/passwords.csv"

    def read_file(self) -> list[list[str]]:
        """Read all password rows from the CSV file. Returns a list of rows, where each row is a list of strings."""
        with open(self.FILE_PATH, 'r', newline='', encoding="utf-8") as csvfile:
            return list(csv.reader(csvfile))
        