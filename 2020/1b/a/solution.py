'''
ideas:
- search
- bit representation xors or something (not as straightforward
because need to take into account subtraction)
- reverse search (start from higher numbers to fail fast)

lol botched
'''

import heapq
from copy import copy

def closest_power_of_2(n):
    if n == 0:
        return 0
    g = 2 ** n.bit_length()
    return n if g % n == 0 else g

def solve3(x0, y0):
    abs_x, abs_y = abs(x0), abs(y0)
    sgn_x, sgn_y = x0 > 0, y0 > 0
    # TODO: handle closest_power_of_2 case
    p2x = closest_power_of_2(abs_x)
    candidates_x = [abs_x, p2x - abs_x]
    p2y = closest_power_of_2(abs_y)
    candidates_y = [abs_y, p2y - abs_y]

    p = None
    print(abs_x ^ abs_y)
    print(abs_x ^ (p2y - abs_y))
    if (abs_x ^ abs_y) == max(p2x, p2y) - 1:
        # additive on both
        p = path2((abs_x, sgn_x, 'WE'), (abs_y, sgn_y, 'SN'))
    elif (abs_x ^ p2y - abs_y) == max(p2x, p2y) - 1:
        # subtractive on y
        p = path2(
            (abs_x, sgn_x, 'WE'),
            (p2y - abs_y, not sgn_y, 'SN'),
            (p2y, sgn_y, 'SN')
        )
    elif (p2x - abs_x ^ abs_y) == max(p2x, p2y) - 1:
        # subtractive on x
        p = path2(
            (abs_x, sgn_x, 'WE'),
            (p2x - abs_x, not sgn_x, 'WE'),
            (p2y, sgn_y, 'SN')
        )
    elif (p2x - abs_x ^ p2y - abs_y) == max(p2x, p2y) - 1:
        # subtractive on x, y
        # TODO?
        p = path2(
            (abs_x, sgn_x, 'WE'),
            (p2x - abs_x, not sgn_x, 'WE'),
            (p2x - abs_y, not sgn_y, 'SN'),
            (p2y, sgn_y, 'SN')
        )
    else:
        return 'IMPOSSIBLE'

    try:
        p = list(p)
    except AssertionError:
        # return 'IMPOSSIBLE'
        raise
    return p

def path2(*components):
    print("path2", components)
    bit_reprs = [bin(x) for x, sgn, dirs in components]

    for i in range(max(len(b) for b in bit_reprs) - 2):
        bits = [b[-i - 1] for b in bit_reprs]
        assert sum(b == '1' for b in bits) == 1

        j = bits.index('1')
        x, sgn, dir = components[j]
        yield dir[int(sgn)]

def path(x, y):
    print("path", x, y)
    bx, by = bin(x), bin(y)
    p = []
    for i in range(max(len(bx), len(by)) - 2):
        if bx[-i - 1] == by[-i - 1] == '1':
            print('should not happen %s %s %s %s' % (x, y, bx, by))
            print(p)
            assert 0
        elif bx[-i - 1] == '1':
            p.append('E')
        elif by[-i - 1] == '1':
            p.append('N')
        else:
            print('should not happen %s %s %s %s' % (x, y, bx, by))
            print(p)
            assert 0
    return p

def reverse(path, reverse_x = False, reverse_y = False):
    if not reverse_x and not reverse_y:
        return path
    new_path = []
    for jump in path:
        if jump == 'E' and reverse_x:
            new_path.append('W')
        elif jump == 'W' and reverse_x:
            new_path.append('E')
        elif jump == 'N' and reverse_y:
            new_path.append('S')
        elif jump == 'S' and reverse_y:
            new_path.append('N')
        else:
            new_path.append(jump)
    return new_path

def solve2(x0, y0):
    '''
    bit repr. only two methods: add or subtract from higher base
    subtract only necessary for odd?
    '''
    x00, y00 = abs(x0), abs(y0)
    rx, ry = x0 < 0, y0 < 0
    xp, yp = closest_power_of_2(x00), closest_power_of_2(y00)
    mp = max(xp, yp)
    x0n = xp - x00
    y0n = yp - y00
    print('xp, yp, x0n, y0n', xp, yp, x0n, y0n)
    if (x00 ^ y00) + 1 == mp:
        # additive
        return reverse(path(x00, y00), rx, ry)
    elif (x00 ^ y0n) + 1 == mp:
        # subtractive on y
        return reverse(reverse(path(x00, y0n), reverse_y = True) + ['N'], rx, ry)
    elif (x0n ^ y00) + 1 == mp:
        # subtractive on x
        return reverse(reverse(path(x0n, y00), reverse_x = True) + ['E'], rx, ry)
    elif (x0n ^ y0n) + 1 == mp: # QUESTIONABLE
        # subtractive on both
        # TODO: when to add extra steps?
        return reverse(reverse(path(x0n, y0n), reverse_x = True) + ['E'], rx, ry)
    else:
        return ['IMPOSSIBLE']

# def neighbors(x, y, jump):
#     yield (x - jump, y, 'S')
#     yield (x + jump, y, 'N')
#     yield (x, y - jump, 'W')
#     yield (x, y + jump, 'E')
#
# def solve(x0, y0):
#     queue = [(min(abs(x0), abs(y0)), 0, 0, [])]
#     while queue:
#         # print('queue', queue)
#         _, x, y, path = heapq.heappop(queue)
#         print('x y path', x, y, path)
#         jump = 2 ** len(path)
#         if len(path) > 300:
#             continue
#         elif x == x0 and y == y0:
#             return ''.join(path.reverse())
#         else:
#             for x1, y1, dir in neighbors(x, y, jump):
#                 path1 = copy(path)
#                 path1.append(dir)
#                 heapq.heappush(
#                     queue, (min(abs(x1), abs(y1)), x1, y1, path1)
#                 )
#     return 'IMPOSSIBLE'

T = int(input())
for t in range(T):
    x, y = [int(x) for x in input().split()]
    s = solve3(x, y)
    print(
        'Case #%d: %s' % (
            t + 1,
            ''.join(s),
        )
    )
