def print_table(objects, colnames):
    '''
    Formatted table showing attributes from a list of objects
    '''
    for colname in colnames:
        print('{:>10s}'.format(colname), end=' ')
    print()
    for obj in objects:
        for colname in colnames:
            print('{:>10s}'.format(str(getattr(obj, colname))), end=' ')
        print()
