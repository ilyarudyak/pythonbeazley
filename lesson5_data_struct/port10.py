import csv
import urllib.request


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


portfolio = read_portfolio('portfolio.csv', errors='silent')
# print('Portfolio', portfolio)

total = 0.0
for holding in portfolio:
    total += holding['shares'] * holding['price']

unique_names = {holding['name'] for holding in portfolio}
namestr = ','.join(unique_names)
u = urllib.request.urlopen(
    'http://finance.yahoo.com/d/quotes.csv?s={}&f=l1'.format(namestr))
data = u.read()
pricedata = data.split()
prices = {name:float(price) for name, price in zip(unique_names, pricedata)}
current_value = sum([holding['shares'] * prices[holding['name']] for holding in portfolio])
change = current_value - total


print(change)
