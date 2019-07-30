#!/usr/local/bin/python3
# https://code.google.com/codejam/contest/6224486/dashboard#s=p0&a=0

T = int(input())
for t in range(T):
    sMax, s = input().split()
    sMax = int(sMax)
    s = [int(c) for c in s]

    numRequired = 0
    numClapping = 0
    for shyness, numOfShyness in enumerate(s):
        # print(shyness, numOfShyness, numClapping, numRequired)
        if shyness > numClapping:
            # print('need more friends!')
            numRequired += shyness - numClapping
            numClapping += shyness - numClapping
        numClapping += numOfShyness

    print('Case #{}: {}'.format(t + 1, numRequired))
