# Small: SUCCESS
# Large: SUCCESS

import itertools
import numpy as np

def solve_case(strings):
    charsets, run_lens = [], []
    for string in strings:
        groupby = [(c, list(it)) for c, it in itertools.groupby(string)]
        charsets.append(c for c, it in groupby)
        run_lens.append(len(it) for c, it in groupby)
    chars = list(itertools.izip_longest(*charsets))
    for char in chars:
        if not all(c == char[0] for c in char):
            return 'Fegla Won'

    total = 0
    run_lens_by_char = zip(*run_lens)
    for char_run_len in run_lens_by_char:
        median = np.median(char_run_len)
        total += sum(abs(x - median) for x in char_run_len)
    return int(total)

def main():
    T = int(raw_input())
    for t in xrange(T):
        N = int(raw_input())
        strings = []
        for n in xrange(N):
            strings.append(raw_input().strip())
        print 'Case #{}:'.format(t + 1),
        print solve_case(strings)

if __name__ == '__main__':
    main()
