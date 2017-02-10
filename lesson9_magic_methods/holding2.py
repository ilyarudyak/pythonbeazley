import csv


class Holding(object):
    def __init__(self, name, date, shares, price):
        self.name = name
        self.date = date
        self.shares = shares
        self.price = price

    def __repr__(self):
        return 'Holding({!r}, {!r}, {!r}, {!r})'.format(self.name, self.date, self.shares, self.price)

    def __str__(self):
        return '{} shares of {} at ${:0.2f}'. format(self.shares, self.name, self.price)    
        
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares


class Portfolio(object):
    def __init__(self):
        self.holdings = []

    def __repr__(self):
        return '{!r}'.format(self.holdings)

    def __len__(self):
        return len(self.holdings)

    def __getitem__(self, n):
        if isinstance(n, str):
            return [h for h in self.holdings if h.name == n]
        else:
            return self.holdings[n]

    def __iter__(self):
        return self.holdings.__iter__()

    @classmethod
    def from_csv(cls, filename):
        self = cls()
        with open(filename, 'r') as f:
            rows = csv.reader(f)
            print(rows)
            next(rows)
            for row in rows:
                h = Holding(row[0], row[1], int(row[2]), float(row[3]))
                self.holdings.append(h)
        return self

    def total_cost(self):
        return sum([h.shares * h.price for h in self.holdings])    



