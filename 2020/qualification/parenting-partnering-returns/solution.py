def solve(activities):
    points = [(s, 'start', n) for n, s, e in activities] + [(e, 'end', n) for n, s, e in activities]
    points.sort()
    # print('points', points)

    schedule = [''] * len(activities)
    c = None
    j = None
    for point, type, i in points:
        if type == 'start':
            if c is not None and j is not None:
                return 'IMPOSSIBLE'
            elif c is None:
                c = point
                schedule[i] = 'C'
            elif j is None:
                j = point
                schedule[i] = 'J'
        elif type == 'end':
            whoDidIt = schedule[i]
            if whoDidIt == 'C':
                c = None
            elif whoDidIt == 'J':
                j = None
            else:
                assert 0
        else:
            assert 0
    return ''.join(schedule)

T = int(input())
for t in range(T):
    N = int(input())

    activities = []
    for n in range(N):
        s, e = [int(x) for x in input().split()]
        activities.append((n, s, e))

    schedule = solve(activities)
    print(
        'Case #%d: %s' % (
            t + 1,
            schedule
        )
    )
