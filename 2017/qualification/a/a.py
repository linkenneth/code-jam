# https://code.google.com/codejam/contest/3264486/dashboard#s=p0

def invert(c):
    return '-' if c == '+' else '+'

T = int(input())
for t in range(T):
    s, k = input().split()
    s = [c for c in s]
    k = int(k)

    # can be solved via a greedy algorithm
    # note: this is O(NK). can be further optimized by keeping track of whether
    # we "owe" a flip:
    # https://code.google.com/codejam/contest/3264486/dashboard#s=a&a=0
    n = 0
    for i in range(len(s)):
        # print(i, s)
        if s[i] == '+':
            continue
        elif i + k > len(s):
            break
        else:
            for j in range(k):
                s[i + j] = invert(s[i + j])
            n += 1

    if s == ['+'] * len(s):
        print('Case #{}: {}'.format(t + 1, n))
    else:
        print('Case #{}: IMPOSSIBLE'.format(t + 1))
