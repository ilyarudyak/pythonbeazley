import csv


def read_portfolio(filename, errors='warn'):
    '''
    Read a csv file into a list ...
    '''

    if errors not in {'warn', 'silent'}:
        raise ValueError("errors must be on of: 'warn', 'silent'")

    portfolio = []      # List of records
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        next(f)       # Skip the header row
        for rowno, row in enumerate(rows, start=1):
            rowno += 1
            try:
                row[2] = int(row[2])
                row[3] = float(row[3])
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row', row)
                    print('Row:', rowno, 'Reason:', err)
                continue
            record = tuple(row)
            portfolio.append(record)
    return portfolio


portfolio = read_portfolio('portfolio.csv', errors='silent')
# print('Portfolio', portfolio)

total = 0.0
# for holding in portfolio:
#     total += holding[2] * holding[3]

for name, date, shares, price in portfolio:
    total += shares * price

print('Total cost:', total)
