import math
import time


# returns the nth fibonacci number
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def fib_better(n):
    fib = 1
    fib2 = 2
    sum = 0
    temp = 0
    i = 0
    while temp < n:
        temp = fib2 + fib
        fib = fib2
        fib2 = temp
        i += 1
        sum += temp
        # print(i, temp)

    print("Sum: ", sum)


def fib_best(n):
    phi = (1 + math.sqrt(5)) / 2
    psi = -1 / phi
    return (phi ** n - psi ** n) / math.sqrt(5)


i = 4
temp = 0
sum = 0
time_s = time.time()
while temp < 400000000:
    temp = fib(i)
    i += 1
    sum += temp
    # print(i, temp)
time_e = time.time() - time_s
print(sum, "\n", "Mediocre Time: ", time_e * 1000, "ms\n")

time_s = time.time()
fib_better(400000000)
time_e = time.time() - time_s
print("Better Time: ", time_e * 1000, "ms")

i = 4
temp = 0
sum = 0
time_s = time.time()
while temp < 400000000:
    temp = fib_best(i)
    i += 1
    sum += temp
    # print(i, temp)
time_e = time.time() - time_s
print(sum, "\n", "Best", time_e * 1000, "ms\n")
