'''
Plan:
- find matching pairs of bits, and track their changes over time
- once you find two pairs of 00 or 11, AND 01 or 10, then you can
determine the total transformations. It's necessary to find the whole
sequence of transformations because you have intermediate data that
you need to transform.
- once you have the 00/11 and 01/10 pairs, you just need to query
one bit from each pair.

00 <-> 11
01 <-> 10

Let D be change and X be no change. DX represents 00 <-> 11 pair changed
but 01 <-> 10 pair did not change.

DD = C
DX = C + I
XD = I
XX = N

- what to do if you can't find the pairs in time? then it doesn't really
matter. That means all your data from before are of one type of pair
(for example, all 00 <-> 11 pairs) and you can just assume the transformation
was EITHER C or C + I
- you can stop when you have all data
'''

from sys import stderr

def C(h, B):
    for k in h.keys():
        h[k] = 1 - h[k]
    return h

def I(h, B):
    # print('h', h, file=stderr)
    for k in h.keys():
        if k > B - k - 1:
            continue
        h[k], h[B - k - 1] = h[B - k - 1], h[k]
    # print('after h', h, file=stderr)
    return h

def CI(h, B):
    return I(C(h, B), B)

def N(h, B):
    return h

# schanged and dchanged
CHANGED_TO_TRANS = {
    (True, True): C,
    (True, False): CI,
    (False, True): I,
    (False, False): N
}

def query(loc):
    print(loc + 1)
    return int(input())

def answer():
    # TODO
    return ''

def solve2(B):
    transformations = []
    queries = []

    same_i = None # 00 <-> 11
    same = None
    diff_i = None # 01 <-> 10
    diff = None

    i = 0
    for round in range(15):
        queries.append({})

        sChanged, dChanged = False, False # None is same as False

        newSame = query(same_i or 0)
        if same_i is not None:
            sChanged = same != newSame
            same = newSame

        newDiff = query(diff_i or 0)
        if diff_i is not None:
            dChanged = diff != newDiff
            diff = newDiff

        # print('same_i, diff_i', same_i, diff_i, file=stderr)
        # print('same, diff', same, diff, file=stderr)
        transformation = CHANGED_TO_TRANS[(sChanged, dChanged)]
        transformations.append(transformation)
        # print('sChanged, dChanged, transformation', sChanged, dChanged, transformation, file=stderr)

        for _ in range(4):
            a = queries[round][i] = query(i)
            b = queries[round][B - i - 1] = query(B - i - 1)

            if same_i is None and a == b:
                same_i = i
                same = a
            if diff_i is None and a != b:
                diff_i = i
                diff = a
            i += 1
        if i > B - i - 1:
            break

    # print(queries, file=stderr)
    # print(transformations, file=stderr)

    # apply transformations TODO
    for round in range(len(queries)):
        for transformation in transformations[round + 1:]:
            # print("applying transformation %s for round %d", transformation, round, file=stderr)
            # print('queries[round]', queries[round], file=stderr)
            queries[round] = transformation(queries[round], B)
            # print('after queries[round]', queries[round], file=stderr)

    # reconstruct array
    answer = [None] * B
    for values in queries:
        for k, v in values.items():
            answer[k] = str(v)
    # print(''.join(answer), file=stderr)
    print(''.join(answer))
    ok = input()

    if ok == 'Y':
        return
    else:
        exit('WRONG ANSWER')

def solve(B):
    # indexes of matching pairs 00 or 11
    same_i = [None, None]
    # indexes of differing pairs 01 or 10
    diff_i = [None, None]

    i = 0
    # map of number of transformations (rounds) to data
    queries = { x: {} for x in range(15) }
    # for round in range(15):
    for round in range(1):
        for _ in range(5):
            # TODO: is random better?
            print(i + 1)
            a = int(input())

            print(B - i)
            b = int(input())

            queries[round]
            i += 1
            print('a, b', a, b, file=sys.stderr)

T, B = [int(x) for x in input().split()]
for t in range(T):
    solve2(B)
