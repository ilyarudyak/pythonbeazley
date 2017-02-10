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
            record = {
                'name': row[0],
                'date': row[1],
                'shares': row[2],
                'price': row[3]
            }
            portfolio.append(record)
    return portfolio



