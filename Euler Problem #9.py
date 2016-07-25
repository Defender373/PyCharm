import time


def is_triple(a, b, c):
    return a ** 2 + b ** 2 == c ** 2 and a < b and b < c


time_s = time.time()
sum = 1000

for a in range(1, sum):
    for b in range(a + 1, sum):
        for c in range(b + 1, sum):
            if is_triple(a, b, c) and a + b + c == 1000:
                print(a, b, c)
                print(a * b * c)

times = time.time() - time_s
print(times)

time_s = time.time()
sum = 1000

for a in range(1, sum):
    for b in range(1, sum):
        for c in range(1, sum):
            if is_triple(a, b, c) and a + b + c == 1000:
                print(a, b, c)
                print(a * b * c)

times = time.time() - time_s
print(times)

time_s = time.time()
sum = 1000

for a in range(1, sum):
    for b in range(a + 1, sum):
        c = b + 1
    while (c ** 2 < b ** 2 + a ** 2):
        c += 1

    if is_triple(a, b, c):
        print(a * b * c)

times = time.time() - time_s
print("Time: ", times)
