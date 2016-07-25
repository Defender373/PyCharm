plist = [2]


def primes(min, max):
    if 2 >= min: yield 2
    for i in range(3, max, 2):
        for p in plist:
            if i % p == 0 or p * p > i: break
            if i % p:
                plist.append(i)
                if i >= min: yield i


def factor(n):
    for prime in primes(2, n):
        if n % prime == 0:
            n /= prime
            yield prime
        if n == 1:
            break


print(max(factor(317584931803)))
