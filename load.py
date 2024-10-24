import pandas as pd
import csv

df = pd.read_csv("btcusdt_1h.csv")

print(df.head())

# Strategy


# Data you want to write (example: list of lists)
data = [
    ['Name', 'Age', 'City'],
    ['Alice', 30, 'New York'],
    ['Bob', 25, 'Los Angeles'],
    ['Charlie', 35, 'Chicago']
]

# Write data to a new CSV file
with open('new_file.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    
    # Write each row of data to the CSV
    writer.writerows(data)