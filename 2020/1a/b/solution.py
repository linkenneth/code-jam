'''
search with backtracking. hwo to 10^9?

pascal triangle each row sum is 2**n for nth row
total sum is 2**(n-1) - 1
'''

from copy import copy
from math import factorial
# from collections import deque
import heapq

def nChooseK(n, k):
    return factorial(n) / factorial(n - k) / factorial(k)

def solve(N):
    full_rows = N.bit_length() - 1

    s = 0
    r, c = 0, 0
    while r < full_rows:
        while c <= r:
            print(r + 1, c + 1)
            s += nChooseK(r, c)
            # print('s', s)
            c += 1
        r += 1
        c += 1
        if r >= full_rows:
            break
        while c > 0:
            c -= 1
            print(r + 1, c + 1)
            s += nChooseK(r, c)
            # print('s', s)
        r += 1

    def neighbors(r, c, s, visited):
        if r - 1 > full_rows:
            if c > 0 and (r - 1, c - 1) not in visited:
                yield (r - 1, c - 1)
            if c <= r - 1 and (r - 1, c) not in visited:
                yield (r - 1, c)
        if c > 0 and (r, c - 1) not in visited:
            yield (r, c - 1)
        if c + 1 <= r and (r, c + 1) not in visited:
            yield (r, c + 1)
        if (r + 1, c) not in visited:
            yield (r + 1, c)
        if (r + 1, c + 1) not in visited:
            yield (r + 1, c + 1)

    queue = [(-s, s, r, c, set(), [])]
    while queue:
        _, s, r, c, visited, path = heapq.heappop(queue)
        # print('queue', queue)
        # print('r, c, s, visited, path', r, c, s, visited, path)
        if s == N:
            for r, c in path:
                print(r + 1, c + 1)
            return
        for r0, c0 in neighbors(r, c, s, visited):
            s0 = s + nChooseK(r0, c0)
            # print('neihgbor, r0, c0, s0', r0, c0, s0)
            if s0 <= N:
                # if s0 == N:
                #     print("+++++ NNN")
                v0 = copy(visited)
                p0 = copy(path)
                v0.add((r, c))
                p0.append((r, c))
                heapq.heappush(queue, (-s0, s0, r0, c0, v0, p0))

    print('final s', s)
    assert 0


T = int(input())
for t in range(T):
    N = int(input())

    print(
        'Case #%d:' % (
            t + 1,
        )
    )
    solve(N)
