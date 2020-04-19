'''
ideas:
- constraints: build a list of radial / circular constraints.
continually select points which reduces the possible area by half
- issues: how to calculate possible areas? how to determine
dart points to throw at?
- optimizations: select the 4 quarter-points on axis in very
first round of darts to quickly determine hemisphere
'''

def solve(s):
    pass

T = int(input())
for t in range(T):
    N = int(input())

    P = []
    for n in range(N):
        P.append(input())

    s = solve(P)
    print(
        'Case #%d: %s' % (
            t + 1,
            s,
        )
    )
