def solve(N):
    a1 = []
    a2 = []
    for i in N:
        if i == '4':
            a1.append('2')
            a2.append('2')
        else:
            a1.append(i)
            a2.append('0')
    return a1, a2

T = int(raw_input())
for t in xrange(T):
    N = raw_input()
    a1, a2 = solve(N)
    print 'Case #%d: %s %s' % (
        t + 1,
        ''.join(a1),
        ''.join(a2).lstrip('0'),
    )
