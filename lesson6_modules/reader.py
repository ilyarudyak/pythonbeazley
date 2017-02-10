import csv


def read_csv(filename, types, *, errors='warn'):
    '''
    Read a csv file into a list ...
    '''

    if errors not in {'warn', 'silent'}:
        raise ValueError("errors must be on of: 'warn', 'silent'")

    records = []      # List of records
    with open(filename, 'r') as f:
        rows = csv.reader(f)
        headers = next(rows)       # Skip the header row
        # print(headers)
        for rowno, row in enumerate(rows, start=1):
            rowno += 1
            try:
                row = [func(val) for func, val in zip(types, row)]
                # print(row)
            except ValueError as err:
                if errors == 'warn':
                    print('Row:', rowno, 'Bad row', row)
                    print('Row:', rowno, 'Reason:', err)
                continue
            record = dict(zip(headers, row))
            records.append(record)
    return records



