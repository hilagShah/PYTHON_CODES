import csv

filename = "sample.csv"


header = ['Name', 'Age', 'City']
rows = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Los Angeles'],
    ['Charlie', 28, 'Chicago']
]

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(header)
    writer.writerows(rows)

print(f"CSV file '{filename}' created successfully. You can open it in Excel.")
