# Much to learn as a "general" way to solve these problems.
# https://code.google.com/codejam/contest/2994486/dashboard#s=a&a=1
#
# Small: SUCCESS
# Large: SUCCESS

from lru_cache import lru_cache

def bit(n, i):
    return (n >> i) & 1

def count(M):
    return _count(M, 31, False)

@lru_cache(maxsize = None)
def _count(M, i, lessThanM):
    '''
    This function does not solve the problem. Instead, it solves the
    problem, "how many non-negative integers are there less than
    M". Trivially, the solution is of course M, but we want to do it
    through enumerating these integers (or sets of integers) in a way such
    that we can use this method to solve similar problems.

    Note: there is no need to store the generated string (though you can
    definitely do it). This way makes it easier to directly use lru_cache
    to memoize results.

    @params
      M : M
      i : index of current bit being counted
      lessThanM : whether the prefix of m (currently generated sequence)
                  before position i is (strictly) less than prefix before
                  position i of M
    @returns M
    '''
    if i == -1:
        # at this point the entire bit string is generated. we only count
        # this string if it's strictly less than M
        return lessThanM
    b = bit(M, i)
    count = 0
    if lessThanM or b == 1:
        # the next sequence is less than M only if it was already less than
        # M, since we chose the current bit as 1 in this case
        count += _count(M, i-1, lessThanM)
    # selected sequence will be less than M if M[i] == 1 and m[i] == 0
    count += _count(M, i-1, lessThanM or b == 1)
    return count

def count_pairs(A, B, K):
    return _count_pairs(64, False, A, False, B, False, K)

@lru_cache(maxsize = None)
def _count_pairs(i, lessA, A, lessB, B, lessK, K):
    '''
    The new rules are:
    1) You can always use (0, 0).
    2) You can use (1, 0) if A[i] == 1 or we are less than A already
    3) You can use (0, 1) if B[i] == 1 or we are less than B already
    4) You can use (1, 1) if both conditions above,
           and K[i] == 1 and we are less than K already.
    '''
    if i == -1:
        return lessA and lessB and lessK
    bit_a, bit_b, bit_k = bit(A, i), bit(B, i), bit(K, i)
    nextLessA = lessA or bit_a == 1
    nextLessB = lessB or bit_b == 1
    nextLessK = lessK or bit_k == 1
    # case 1
    count = _count_pairs(i-1, nextLessA, A, nextLessB, B, nextLessK, K)
    if nextLessA:  # case 2
        count += _count_pairs(i-1, lessA, A, nextLessB, B, nextLessK, K)
    if nextLessB:  # case 3
        count += _count_pairs(i-1, nextLessA, A, lessB, B, nextLessK, K)
    if nextLessA and nextLessB and nextLessK:  # case 4
        count += _count_pairs(i-1, lessA, A, lessB, B, lessK, K)
    return count

def solve_case(A, B, K):
    return count_pairs(A, B, K)

def main():
    T = int(raw_input())
    for t in xrange(T):
        A, B, K = map(int, raw_input().split())
        print 'Case #{}:'.format(t + 1),
        print solve_case(A, B, K)

if __name__ == '__main__':
    main()
