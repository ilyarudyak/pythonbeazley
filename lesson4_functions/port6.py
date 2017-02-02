import csv


def portfolio_cost(filename, *, errors='warn'):
    '''
    Computes total ...
    '''

    if errors not in {'warn', 'silent'}:
        raise ValueError("errors must be on of: 'warn', 'silent'")

    total = 0.0
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
            total += row[2] * row[3]
    return total


total = portfolio_cost('missing.csv', errors='silen')
print('Total cost', total)
