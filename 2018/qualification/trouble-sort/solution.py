from collections import defaultdict

def solve(values):
    # print 'solve(values)', values
    evens = sorted(values[::2])
    odds = sorted(values[1::2])
    tSorted = []
    for i in xrange(max(len(evens), len(odds))):
        if i < len(evens):
            tSorted.append(evens[i])
        if i < len(odds):
            tSorted.append(odds[i])
    for i in xrange(len(tSorted) - 1):
        if tSorted[i] > tSorted[i + 1]:
            return i
    return 'OK'

T = int(raw_input())
for t in xrange(T):
    D = int(raw_input())
    values = [int(x) for x in raw_input().split()]
    print 'Case #%d: %s' % (
        t + 1,
        solve(values)
    )
