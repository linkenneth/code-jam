def solve(s):
    sp = []
    depth = 0
    for x in s:
        # print('x', x)
        while depth < x:
            sp.append('(')
            depth += 1
        while depth > x:
            sp.append(')')
            depth -= 1
        sp.append(str(x))
    while depth > 0:
        sp.append(')')
        depth -= 1
    return ''.join(sp)

T = int(input())
for t in range(T):
    S = [int(x) for x in input()]

    # print(S)
    Sp = solve(S)
    # print(Sp)
    print(
        'Case #%d: %s' % (
            t + 1,
            Sp
        )
    )
