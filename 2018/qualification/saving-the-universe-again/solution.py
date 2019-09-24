def damage(P):
    d = 0
    m = 1
    for c in P:
        if c == 'C':
            m <<= 1
        elif c == 'S':
            d += m
        else:
            assert 0
    return d

def solve(D, P):
    '''
    DP. Find # of S's >= this position for each position. Go through C's
    from the back and reduce by multiplier count
    '''
    # print 'solve(D, P)', D, P

    hacks = 0
    L = [-1] * len(P)
    sCount = 0
    lastCIndex = -1
    multiplier = 1
    for i in xrange(len(P) - 1, -1, -1):
        if P[i] == 'S':
            sCount += 1
        L[i] = sCount

        # find last C and its multiplier
        if P[i] == 'C':
            multiplier <<= 1
            if lastCIndex == -1:
                lastCIndex = i

    diff = damage(P) - D
    i = lastCIndex
    # print 'diff', diff
    while i >= 0 and diff > 0:
        # print 'i', i
        if P[i] == 'C':
            if L[i] > 0:
                diff -= multiplier / 2
                L[i] -= 1
                hacks += 1
                # print 'hack @', i, diff, L[i]
            else:
                multiplier >>= 1
                # print 'multiplier decrease', multiplier
                i -= 1
        else:
            i -= 1

    if diff > 0:
        return 'IMPOSSIBLE'
    return hacks

T = int(raw_input())
for t in xrange(T):
    D, P = raw_input().split()
    D = int(D)
    print 'Case #%d: %s' % (
        t + 1,
        solve(D, P)
    )
