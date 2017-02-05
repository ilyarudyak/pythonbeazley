# Python programming language

## Lesson 2. Program structure and execution model

* formatting output (`>` - alignment right, `d` - integer, `f` - float, `10.2` - len of the field is 10, 2 digits after dot):
```python
print('{:>5s} {:>10s} {:>10s} {:>10s}'
      .format('Month', 'Interest', 'Principal', 'Remaining'))

print('{:>5d} {:>10.2f} {:>10.2f} {:>10.2f}'
          .format(month, interest, total_payment - interest, principal))
```
```
Month   Interest  Principal  Remaining
    1    2083.33    1600.78  498399.22
    2    2076.66    1607.45  496791.78
    3    2069.97    1614.14  495177.63
    4    2063.24    1620.87  493556.76
    5    2056.49    1627.62  491929.14
    6    2049.70    1634.41  490294.73
    7    2042.89    1641.22  488653.52
    8    2036.06    1648.05  487005.46
```
* print to the file (instead of console):
```python
with open('schedule2.txt', 'w') as out:
  print('{:>5s} {:>10s} {:>10s} {:>10s}'
        .format('Month', 'Interest', 'Principal', 'Remaining'), file=out)
```
## Lesson 3. Text processing and files

* two main options to work with file: (a) read entire file or (b) read it line by line:
```python
with open('portfolio.csv', 'r') as f:
  data = f.read()
  ...
  
with open('portfolio.csv', 'r') as f:
    headers = next(f)         #Skip first line with headers
    for line in f:
      line = line.strip()     # Remove '\n'
      ...
```
* strip double quotes, convert to `int` and `float`:
```python
parts[0] = parts[0].strip('"')
parts[2] = int(parts[2])
parts[3] = float(parts[3])
```
* using csv module (instead of working on the low level):
```python
import csv

with open('portfolio2.csv', 'r') as f:
    rows = csv.reader(f)      # [['name', 'date', 'shares', 'price'], ['AA', 'June 11, 2007', '100', '32.20'], ...
    headers = next(f)
    for row in rows:
        row[2] = int(row[2])
        ...
```
## Lesson 4. Functions and error handling
* using `glob` module to iterate over files:
```python
import glob

files = glob.glob('prtfolio*.csv')
for filename in files:
      print(filename, portfolio_cost(filename))
      ...
```
* error handling in python:
```python
try:
    row[2] = int(row[2])
    row[3] = float(row[3])
except ValueError as err:
    print('Row:', rowno, 'Error:', err)
    continue      # Skip to the next row
```
* using `enumerate()` instead of creating some counter:
```python
rows = csv.reader(f)    # [['name', 'date', 'shares', 'price'], ['AA', 'June 11, 2007', '100', '32.20'], ...
for rowno, row in enumerate(rows, start=1):
      ...
```
* why should we use specific exception instead of `Exception` ('diaper pattern')?
```python
try:
    row[2] = int(row[2])
    row[3] = flot(row[3])     # This mistake (flot instead float) will also be catched. This is not FAIL FAST.
except Exception as err:
    print('Row:', rowno, 'Error:', err)
    continue      # Skip to the next row
```
* force to use keyword argument:
```python
def portfolio_cost(filename, *, errors='warn'):       # Force to use keyword argument
      if errors not in {'warn', 'silent'}:            # Defensive programming
            raise ValueError("errors must be on of: 'warn', 'silent'")
      ...
# total = portfolio_cost('missing.csv', 'silent') - error
total = portfolio_cost('missing.csv', errors='silent')
```
* if you can not handle exception just don't do this; it will be handled by another (higher-level) process;

## Lesson 5. Data structures and data manipulation
* tuple is like an entry in database (different types are common); main operations - packing and unpacking;
* in lists entries are usually of the same type;
* set eliminates duplicates and this is its main use;the other one - membership testing;
* we may read file into list of tuples but in this case we have to unpack a lot of positions:
```python
...
record = tuple(row)
portfolio.append(record)
...

for name, date, shares, price in portfolio:     # We have to unpack 4 values but need only 2
    total += shares * price
```
* better solution would be to use list of dictionaries:
```python
...
record = {
    'name': row[0],
    'date': row[1],
    'shares': row[2],
    'price': row[3]
}
...
for holding in portfolio:
    total += holding['shares'] * holding['price']
```
* and in the last case we can transfer our data structure as json:
```python
import json

data = json.dumps(portfolio)  # Just a string
port = json.loads(data)
```
portfolio.append(record)
## Lesson 6. Library functions and import
## Lesson 7. Classes and objects
## Lesson 8. Inheritance
## Lesson 9. Python magic methods
## Lesson 10. Encapsulation
## Lesson 11. Higher order functions and closures
## Lesson 12. Metaprogramming and decorators
## Lesson 13. Metaclasses
## Lesson 14. Iterators and generators
## Lesson 15. Coroutines
