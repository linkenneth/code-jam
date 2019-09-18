'''
Notes: the way I solved this problem is to have converted it into two
one-dimensional skyline problems. However, the other ways of solving it
in O(P^2) time is also interesting, by using the O(Q^2) time solution but
noticing that the only squares that require checking are the ones that are
one square east of someone or 0.

Ah, also just read the linear time solution, which is slightly different
from mine. Instead of using intervals that end at 0 or Q, they just preprocess
data into (C, W, E) and work through sorted list of this. O(P) possible tuples,
also sorting time. Much simpler than mine. Mine solves a more general problem
than is required.

Interesting problem though with extensions into the real world. Consider a
better model where each person heading in a direction creates a density
graph of different weights for where they want to go. Use this in Citizen
for example to find interesting events (or dangers) happening around the city.
'''

def countDisjoint(intervals, Q):
    '''
    (0, 5), (0, 6), (4, 10) => (0, 3), (4, 4), (5, 5), (6, 6), (7, 10)
    '''
    # https://stackoverflow.com/questions/4542892
    # also this is quite literally the skyline problem
    if not intervals:
        return [(0, Q, 0)]

    points = []  # points of interest
    for start, end in intervals:
        points.append(('start', start))
        points.append(('end', end))
    points.sort(key=lambda (type, value): (value, type == 'end'))
    # print 'points', points

    count = 0
    last = None
    disjoints = []
    for type_, value in points:
        # print count, last, type_, value
        if type_ == 'start':
            if last is not None and last <= value - 1:
                disjoints.append( (last, value - 1, count) )
            count += 1
            last = value
        elif type_ == 'end':
            if last is not None and last <= value:
                disjoints.append( (last, value, count) )
            count -= 1
            last = value + 1
    # above algorithm short-counts last point, so adjust
    # print 'disjoints', disjoints
    disjoints[-1] = (disjoints[-1][0], disjoints[-1][1] + 1, disjoints[-1][2])
    return disjoints

def solve(P, Q, people):
    # print P, Q, people

    # 1. convert people to x- and y-intervals (inclusive intervals)
    xIntervals = []
    yIntervals = []
    for x, y, d in people:
        if d == 'N':  # increasing y
            yIntervals.append((y + 1, Q))
        elif d == 'S':  # decreasing y
            yIntervals.append((0, y - 1))
        elif d == 'E':  # increasing x
            xIntervals.append((x + 1, Q))
        elif d == 'W':  # decreasing x
            xIntervals.append((0, x - 1))
    # print 'xIntervals', xIntervals
    # print 'yIntervals', yIntervals

    # 2. break into sub-intervals accordingly and assign each sub-interval
    # with a count of frequency
    xDisjoint = countDisjoint(xIntervals, Q)
    yDisjoint = countDisjoint(yIntervals, Q)

    # for start, end, count in xDisjoint:
    #     print 'x', start, end, count
    #     # if not disjointIntervals
    # for start, end, count in yDisjoint:
    #     print 'y', start, end, count

    # 3. find most common sub-interval for each of x and y
    xMode = max(xDisjoint, key=lambda (start, end, count): count)
    yMode = max(yDisjoint, key=lambda (start, end, count): count)
    # print 'xMode, yMode', xMode, yMode

    # 4. return the most southwestern point of most common sub-interval
    return xMode[0], yMode[0]

T = int(raw_input())
for t in xrange(T):
    P, Q = [int(x) for x in raw_input().split()]
    people = []
    for p in xrange(P):
        x, y, d = raw_input().split()
        x, y = int(x), int(y)
        people.append((x, y, d))
    print 'Case #%d: %s' % (
        t + 1,
        ' '.join(map(str, solve(P, Q, people)))
    )
