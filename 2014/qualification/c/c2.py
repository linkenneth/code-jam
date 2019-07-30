# THIS SOLUTION DOESN'T WORK. but it's close.

from Queue import PriorityQueue

def make_board(R, C):
    return [['.'] * C for _ in xrange(R)]

def make_queue(board):
    ''' Makes a queue of all the positions on the board, with the number of
    "openings" it contains. An "opening" is the number of spots on the
    board that, if occupied by a mine, would render this current cell a
    number cell (1-8). '''
    queue = PriorityQueue()
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            openings = max_openings((i, j), board)
            queue.put((openings, i, j))
            board[i][j] = openings
    return queue

def max_openings(cell, board):
    # shortcut to calculate openings in the beginning
    i, j = cell
    row_edge = i == 0 or i == (len(board) - 1)
    col_edge = j == 0 or j == (len(board[0]) - 1)
    openings = 8
    openings -= (row_edge or col_edge) * 3
    openings -= (row_edge and col_edge) * 2
    return openings

def calculate_openings(cell, board):
    i, j = cell
    openings = 0
    for ni, nj in neighbors((i, j), board):
        if board[ni][nj] != '*':
            openings += 1
    return openings

def print_board(board):
    for row in board:
        print ''.join(str(c) for c in row)

def solve_case(R, C, M):
    board = make_board(R, C)
    queue = make_queue(board)
    # TODO remove queue items

    i, j = 0, 1

    mines_placed = 0
    while not queue.empty():
        if mines_placed == M:
            break
        openings, i, j = queue.get()
        if board[i][j] == '*':
            continue
        board[i][j] = '*'
        for ni, nj in neighbors((i, j), board):
            if board[ni][nj] == '*':
                continue
            openings = calculate_openings((ni, nj), board)
            board[ni][nj] = openings
            queue.put((openings, ni, nj))
        mines_placed += 1

    possible = False
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == max_openings((i, j), board):
                board[i][j] = 'c'
                possible = True
                break
        if possible:
            break

    if possible:
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell != 'c' and cell != '*':
                    board[i][j] = '.'
        print_board(board)
    else:
        print 'Impossible'
        print_board(board)

def neighbors(cell, board):
    for i in xrange(-1, 2):
        r = cell[0] + i
        if not (0 <= r < len(board)): continue
        for j in xrange(-1, 2):
            c = cell[1] + j
            if not (0 <= c < len(board[0])): continue
            elif i == j == 0: continue
            yield (r, c)

def main():
    T = int(raw_input())
    for t in xrange(T):
        R, C, M = map(int, raw_input().split())
        print 'Case #{}:'.format(t + 1)
        solve_case(R, C, M)

if __name__ == '__main__':
    main()
