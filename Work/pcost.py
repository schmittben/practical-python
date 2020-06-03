import csv
import sys

def portfolio_cost(filename):
    f = open(filename)
    total_cost = 0
    rows = csv.reader(f)
    headers = next(rows)

    for row in rows:
        total_cost += int(row[1]) * float(row[2])

    return total_cost

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'

cost = portfolio_cost(filename)
print("Total cost of portfolio: ", cost)