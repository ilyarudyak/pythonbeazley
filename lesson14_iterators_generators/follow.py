import os
import time

def follow(filename):
    f = open(filename, 'r')
    f.seek(0, os.SEEK_END)

    while True:
        line = f.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

for line in follow('/var/log/system.log'):
    print(line, end='')