import csv


file_path = "/Users/krissi/Documents/GitHub/skvis/main/IO/database.csv" # Replace with your CSV file name


import csv

with open(file_path, 'r', newline='') as csvfile:
    csv_reader = csv.reader(csvfile)

    # If the first row contains headers, you can read them separately
    headers = next(csv_reader)
    print(f"Headers: {headers}")

    for row_index, row in enumerate(csv_reader):
        print(f"Row {row_index + 1}:")
        for col_index, value in enumerate(row):
            print(f"  Column {col_index} ({headers[col_index] if headers else 'N/A'}): {value}")