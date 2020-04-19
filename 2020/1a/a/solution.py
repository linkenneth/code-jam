'''
common suffix and prefix. prefix / suffix gate

keep track of all segments. reduce sub-segments
'''

import re

def allSubString(ss):
    'false if not all substrings, otherwise longest substring'
    for s1 in ss:
        if s1 == '*':
            continue
        for s2 in ss:
            if s2 == '*':
                continue
            c1 = s1.strip('^').strip('$')
            c2 = s2.strip('^').strip('$')
            if c1 == '' or c2 == '':
                continue
            if s1 not in s2 and s2 not in s1:
                return False
    max_ = max(len(s) for s in ss)
    for s in ss:
        if len(s) == max_:
            return s
    assert -1

# def solve2(P):
#     '''
#     look simultaneously across seegments
#     for each segmetn comparison, if not all substrings of each other
#     fail.
#     if all substrings, take the largest one (superstring)
#     advance everything
#     '''

def solve(P):
    strings = []
    indices = []

    for p in P:
        # TODO: adjacent **?
        segments = re.split('(\*)', ('^' + p + '$'))
        strings.append(segments)

    result = []
    indices = [0] * len(strings)
    while True:
        ss = []
        # print('strings', strings)
        for segments, i in zip(strings, indices):
            if i >= len(segments):
                ss.append('')
            else:
                ss.append(segments[i])
        if all(s == '' for s in ss):
            return ''.join(result).strip('^').strip('$')

        # ss = [string[i] for string, i in zip(strings, indices)]
        print('ss', ss)
        superstring = allSubString(ss)
        if superstring == '*':
            indices[0] += 1
        elif superstring:
            result.append(superstring)
            indices = [i + 1 for i in indices]
        else:
            return '*'

        # asteriskCount = sum(s == '*' for s in ss)
        # # print('asteriskCount', asteriskCount)
        # # print('len(indices)', len(indices))
        # if asteriskCount == len(indices):
        #     # all asterisk
        #     indices = [i + 1 for i in indices]
        # elif asteriskCount == len(indices) - 1:
        #     # exactly one required string. take
        #     # print("wtf")
        #     i = 0
        #     while True:
        #         if s[i] != '':
        #             break
        #         i += 1
        #     result.append(string[i])
        #     indices[i] += 1
        # else:
        #     # impossible
        #     print(ss)
        #     return '*'

    return result


T = int(input())
for t in range(T):
    N = int(input())

    P = []
    for n in range(N):
        P.append(input())

    s = solve(P)
    print(
        'Case #%d: %s' % (
            t + 1,
            s,
        )
    )
