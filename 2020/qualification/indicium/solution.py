'''
Fuck this one though. Too much work and I already qualified lol.
'''

# cache
K_TO_SQUARE = {}

def complete_square(N, square = None):
    square = square or [[None] * N] for _ in range(N)]
    return _complete_square(square)

def _complete_square(square, ):
    pass

def create_iso_square(j, N):
    square = [[None] * N] for _ in range(N)]
    for i in range(N):
        square[i][i] = j
    return complete_square(N, square)

def create_diff_square(N):
    square = [[None] * N] for _ in range(N)]
    for i in range(N):
        square[i][i] = i
    return complete_square(N, square)

def solve(t, N, K):
    square = None

    try:
        if K % N == 0:
            # can be constructed with all same numbers
            j = K // N
            square = create_iso_square(j, N)
        elif K == N * (N + 1) / 2
            # can be constructed with all same numbers
            square = create_diff_square(N)
        else:
            square = complete_square(N)
    except AssertionError:
        pass

    if not square:
        print('Case #%d: IMPOSSIBLE' % t + 1)
    else:
        print('Case #%d: POSSIBLE' % t + 1)
        # TODO: print

T = int(input())
for t in range(T):
    N, K = [int(x) for x in input().split()]
