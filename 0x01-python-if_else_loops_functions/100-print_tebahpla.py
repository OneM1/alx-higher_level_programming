#!/usr/bin/python3
for i in range(ord('z'), ord('a') - 1, -1):
    if i % 2 == 0:
        adjst = 0
    else:
        adjst = 32
    print('{}'.format(chr(i - adjst)), end='')
