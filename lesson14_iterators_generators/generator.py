def countdown(n):
    print('Counting from', n)
    while n > 0:
        yield n
        n -= 1
    print('Done')

def grep(pattern, filename):
    with open(filename) as f:
        for line in f:
            if pattern in line:
                yield line