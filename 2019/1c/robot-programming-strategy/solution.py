# Given a move, returns the move that counters it.
WINS_AGAINST = {
    'R': 'S',
    'P': 'R',
    'S': 'P',
}

LOSES_AGAINST = {
    'R': 'P',
    'P': 'S',
    'S': 'R',
}

def solve(programs):
    selections = []

    i = 0
    while programs:
        moves = set(program[i % len(program)] for program in programs)
        # print i, programs, moves
        # 0 indicates tie, -1 indicates loss, 1 indicates win. 2 undetermined
        counters = { 'R': 2, 'P': 2, 'S': 2 }
        for move in moves:
            if move == 'R':
                counters['R'] = min(counters['R'], 0)
                counters['P'] = min(counters['P'], 1)
                counters['S'] = min(counters['S'], -1)
            elif move == 'P':
                counters['R'] = min(counters['R'], -1)
                counters['P'] = min(counters['P'], 0)
                counters['S'] = min(counters['S'], 1)
            elif move == 'S':
                counters['R'] = min(counters['R'], 1)
                counters['P'] = min(counters['P'], -1)
                counters['S'] = min(counters['S'], 0)
            else:
                assert 0
        if max(counters.values()) == -1:
            return 'IMPOSSIBLE'
        argmax = max(counters, key=counters.get)
        # print 'selected move', argmax
        selections.append(argmax)
        programs = filter(
            lambda program: WINS_AGAINST[argmax] != program[i % len(program)],
            programs
        )
        i += 1
    return ''.join(selections)

T = int(raw_input())
for t in xrange(T):
    A = int(raw_input())
    programs = []
    for a in xrange(A):
        programs.append(raw_input())
    print 'Case #%d: %s' % (
        t + 1,
        solve(programs)
    )
