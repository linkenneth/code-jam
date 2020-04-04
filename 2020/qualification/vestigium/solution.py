def solve(matrix):
    N = len(matrix)

    k = 0
    r = 0
    c = 0

    for n, row in enumerate(matrix):
        if len(set(row)) != len(row):
            r += 1
        col = [matrix[x][n] for x in range(N)]
        # print('col', col)
        if len(set(col)) != len(col):
            c += 1

    diag = [matrix[x][x] for x in range(N)]
    # print('diago', diag)
    k = sum(diag)
    return k, r, c

T = int(input())
for t in range(T):
    N = int(input())
    matrix = []
    for n in range(N):
        matrix.append([int(x) for x in input().split()])

    k, r, c = solve(matrix)
    print(
        'Case #%d: %d %d %d' % (
            t + 1,
            k,
            r,
            c
        )
    )
