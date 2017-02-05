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

## Lesson 4. Functions and error handling
## Lesson 5. Data structures and data manipulation
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
