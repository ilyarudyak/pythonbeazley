from logcall2 import logged


@logged
def add(x, y):
    return x + y

@logged
def sub(x, y):
    return x - y

@logged
def mul(x, y):
    return x * y