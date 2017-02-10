x = 42

def spam():
    print('spam() is running ... x is', x)

def run():
    print('run() is running ... calling spam()')
    spam()


if __name__ == '__main__':
    print('starting ...')
    run()

