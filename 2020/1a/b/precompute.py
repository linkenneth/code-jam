from math import factorial

# precomputed sums for each row. always ends on (r, 1) where
# r is some row.
possible_sums = {}


def nChooseK(n, k):
    return factorial(n) / factorial(n - k) / factorial(k)
