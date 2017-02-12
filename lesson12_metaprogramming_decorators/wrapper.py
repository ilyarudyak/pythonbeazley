def add(x, y):
    return x + y

def add_wrapper(*args, **kargs):
    print('Wrapping!')
    return add(*args, **kargs)