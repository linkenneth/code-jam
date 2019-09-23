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
    Greedy. Go from front to find last C in sequence of C's. Backtrack and
    continue to swap C's from before. Continue forwards.
    '''
    print 'solve(D, P)', D, P
    if P.count('S') > D:
        return 'IMPOSSIBLE'

    P = list(P)

    diff = damage(P) - D
    hacks = 0
    direction = 'forward'
    multiplier = 1
    i = 0
    while diff > 0:
        print 'i', i
        if P[i] == 'C':
            # multiplier <<= 1
            while i + 1 <= len(P) - 1 and P[i + 1] == 'C':
                multiplier <<= 1
                i += 1
            if i + 1 >= len(P):
                break
            diff -= multiplier
            P[i], P[i + 1] = P[i + 1], P[i]
            print 'P', P
            # diff >>= 1
            # hacks += 1
        elif P[i] == 'S':
            diff -= 1

        if direction is 'forward':
            i += 1
        else:
            i -= 1
    return hacks

T = int(raw_input())
for t in xrange(T):
    D, P = raw_input().split()
    D = int(D)
    print 'Case #%d: %s' % (
        t + 1,
        solve(D, P)
    )
