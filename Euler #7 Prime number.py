import time


def prime(number):
    time_s = time.time()
    primes = [2]
    prime = True
    for i in range(3, number):
        for j in primes:
            if i % j == 0:
                prime = False
        if prime:
            primes.append(i)
        prime = True
    print_time = 1000 * (time.time() - time_s)
    print(print_time)


def prime_faster(n):
    time_s = time.time()
    primes = set(range(2, n))
    for i in range(2, int(n ** .5) + 1):
        for j in range(i * 2, n, i):
            primes.discard(j)
    print_time = 1000 * (time.time() - time_s)
    print(print_time)
    return primes


def prime_fastest(n):
    time_s = time.time()
    numbers = list(range(0, n))
    # i is the prime we are testing
    for i in numbers:
        if i < 2:
            continue
        elif i > n ** 0.5:
            break
        # j is the number being tested against
        for j in range(i ** 2, n, i):
            numbers[j] = 0

    print_time = 1000 * (time.time() - time_s)
    print(print_time)
    return [x for x in numbers if x > 1]


# prime(100000)
print(prime_fastest(100))
