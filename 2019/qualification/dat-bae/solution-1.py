'''
Solution for F = 10 test set.
'''

import sys

def solve(N, B, F):
    formatString = '0%db' % F
    X = [[] for _ in xrange(F)]
    for n in xrange(N):
        bitString = format(n, formatString)
        for f in xrange(F):
            X[f].append(bitString[f])

    I = []
    for f in range(F):
        sys.stdout.write(''.join(X[f]) + '\n')
        sys.stdout.flush()
        I.append(raw_input())

    seen = set([n for n in xrange(N)])
    for i in xrange(N - B):
        bitString = ''.join(I[f][i] for f in xrange(F))
        seen.remove(int(bitString, 2))

    sys.stdout.write(' '.join(str(i) for i in seen) + '\n')
    sys.stdout.flush()
    isCorrect = raw_input()
    assert isCorrect == '1'

T = int(raw_input())
for t in xrange(T):
    N, B, F = (int(x) for x in raw_input().split())
    solve(N, B, F)
