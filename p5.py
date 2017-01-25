from itertools import count, takewhile

def primes(n):
    seen = list()
    for i in xrange(2, n + 1):
        if all(map(lambda prime: i % prime, seen)):
            seen.append(i)
            yield i

def smallest(n):
    result = 1
    for prime in primes(n):
        bprime = max(takewhile(lambda x:x<=n, (prime ** c for c in count(1))))
        result *= bprime
    return result

print smallest(20)
