'''
simulate
'''

def compassNeighbors(matrix, r, c):
    # north
    i = 1
    while r - i >= 0:
        if matrix[r - i][c] is not None:
            yield (r - i, c)
            break
        i += 1
    # south
    i = 1
    while r + i < len(matrix):
        if matrix[r + i][c] is not None:
            yield (r + i, c)
            break
        i += 1
    # west
    i = 1
    while c - i >= 0:
        if matrix[r][c - i] is not None:
            yield (r, c - i)
            break
        i += 1
    # east
    i = 1
    while c + i < len(matrix[0]):
        if matrix[r][c + i] is not None:
            yield (r, c + i)
            break
        i += 1

def solve(matrix):
    interest = 0
    changed = False
    while True:
        total_skill = 0
        to_kill = set()
        for r, row in enumerate(matrix):
            for c, skill in enumerate(row):
                if not skill:
                    continue
                total_skill += skill
                neighbors = list(compassNeighbors(matrix, r, c))
                if not neighbors:
                    continue
                neighboring_skill = sum(matrix[r][c] for r, c in neighbors) / len(neighbors)
                if skill < neighboring_skill:
                    to_kill.add((r, c))
        interest += total_skill
        if not to_kill:
            return interest
        for r, c in to_kill:
            matrix[r][c] = None

T = int(input())
for t in range(T):
    R, C = [int(x) for x in input().split()]

    matrix = []
    for r in range(R):
        matrix.append([int(x) for x in input().split()])

    s = solve(matrix)
    print(
        'Case #%d: %s' % (
            t + 1,
            s,
        )
    )
