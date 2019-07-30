# https://code.google.com/codejam/contest/3274486/dashboard

import math

def radial_area(r):
    return math.pi * r * r

def height_area(r, h):
    return 2 * math.pi * r * h

T = int(input())
for t in range(T):
    n, k = [int(i) for i in input().split()]

    pancakes = []
    for i in range(n):
        r, h = [int(i) for i in input().split()]
        pancakes.append((i, r, h))

    current_max = 0
    for i, r, h in pancakes:
        rest = [(i2, r2, h) for i2, r2, h in pancakes if r2 <= r and i != i2]
        if len(rest) < k - 1:
            continue
        areas = sorted(
            ((i, height_area(r, h)) for i, r, h in rest),
            key=lambda x: x[1],
            reverse=True)
        best = sum(area for i, area in areas[:k-1]) + radial_area(r) + height_area(r, h)
        if best >= current_max:
            current_max = best

    # areas = sorted((i, radial_area(r), height_area(r, h)) for i, r, h in pancakes)
    # max_solo_areas = sorted((i, r + h) for i, r, h in areas)
    # pancakes.sort(key=lambda t: areas[t[0]])
    #
    # current_r = 0
    # for i, (r, h) in enumerate(pancakes):
    #     r_area, h_area = areas[i]
    #
    # first = max_solo_areas[0]
    # first_r, first_h = pancakes.pop(first[0])
    # areas.pop(first[0])
    # max_solo_areas.pop(first[0])

    # # select max area first
    # first = max(enumerate(max_solo_areas), key=lambda x: x[1])
    # first_r, first_h = pancakes.pop(first[0])
    # areas.pop(first[0])
    # max_solo_areas.pop(first[0])
    #
    # # only height_area matters from here
    # # rest = sorted((h for r, h in areas), reverse=True)[:k-1]
    # # print(first, rest)
    # current_r = 0
    # for i, (r, h) in enumerate(pancakes):
    #     r_area, h_area = areas[i]

    print('Case #{}: {}'.format(t + 1, current_max))
