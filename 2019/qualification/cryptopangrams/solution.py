'''
Completed after looking at analysis and being reminded that I can find GCD
between ciphertext entries... But damn is this not a nutty off-by-one error
calapalooza.
'''

def solve(cipher):
    # off by one because we start by comparing second number
    plain = [None]

    # wind forward until numbers are different
    last = cipher[0]
    i = 1
    while cipher[i] == last:
        plain.append(None)
        i += 1

    j = i
    primes = set()
    lastPrime = firstPrime = gcd(last, cipher[j])
    primes.add(last / lastPrime)  # adds a
    while j < len(cipher):
        primes.add(lastPrime)  # adds b
        plain.append(lastPrime)
        lastPrime = cipher[j] / lastPrime
        j += 1
    primes.add(lastPrime)
    plain.append(lastPrime)

    primes = sorted(list(primes))
    key = { p: chr(ord('A') + i) for i, p in enumerate(primes) }

    # backtrack
    lastPrime = firstPrime
    for j in range(i - 1, -1, -1):
        lastPrime = cipher[j] / lastPrime
        plain[j] = lastPrime
        i -= 1

    return ''.join(key[x] for x in plain)

def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

T = int(raw_input())
for t in xrange(T):
    N, L = (int(x) for x in raw_input().split())
    cipher = [int(x) for x in raw_input().split()]
    print 'Case #%d: %s' % (
        t + 1,
        solve(cipher)
    )
