import csv


def portfolio_cost(filename):
    '''
    Computes total ...
    '''

    total = 0.0
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        next(f)       # Skip the header row
        for row in rows:
            row[2] = int(row[2])
            row[3] = float(row[3])
            total += row[2] * row[3]
    return total


total = portfolio_cost('portfolio2.csv')
print('Total cost', total)
