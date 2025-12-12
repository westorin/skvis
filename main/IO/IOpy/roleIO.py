import csv

class RoleIO:
    """Handles reading and writing raw role data to/from CSV."""

    FILE_PATH: str = "main/IO/csv/roles.csv"

    def read_file(self) -> list[list[str]]:
        """Read all role rows from the CSV file. Returns a list of rows, where each row is a list of strings."""
        with open(self.FILE_PATH, 'r', newline='',encoding="utf-8") as csvfile:
            return list(csv.reader(csvfile))
        
    def write_file(self, rows: list[list[str]]) -> None:
        """Overwrite the CSV file with role rows."""
        with open(self.FILE_PATH, 'w', newline='', encoding="utf-8") as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerows(rows)