def solve(L):
    a = []
    for c in L:
        if c == 'E':
            a.append('S')
        elif c == 'S':
            a.append('E')
    return ''.join(a)

T = int(raw_input())
for t in xrange(T):
    N = int(raw_input())
    L = raw_input()
    print 'Case #%d: %s' % (
        t + 1,
        solve(L)
    )
