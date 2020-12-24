import csv
from pathlib import Path

equity_funding = [
    {"Company": "CryptoVisors", "Amount": 200000, "Series": "A"},
    {"Company": "Flutterwave", "Amount": 65000000, "Series": "D"},
    {"Company": "nCino", "Amount": 80000000, "Series": "D"},
    {"Company": "Privacy.com", "Amount": 10000000, "Series": "B"},
]

# Create an empty list called `big_raisers`
# YOUR CODE HERE!
big_raisers = []
# Iterate (loop) through each dictionary in the list of dictionaries.
for equity in equity_funding:
    if equity["Amount"] >= 50000000:
        big_raisers.append(equity)
# print(big_raisers)

header = ["Company", "Amount", "Series"]

csvpath = Path('large_equity_rounds.csv')

print("writting the data to csv file...")

with open(csvpath, "w") as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=",")
    csvwriter.writerow(header)

    for item in big_raisers:
        csvwriter.writerow(item.values())

print(item.keys())


