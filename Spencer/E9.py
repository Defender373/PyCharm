import time


def is_triple(a, b, c):
    return a ** 2 + b ** 2 == c ** 2 and a < b and b < c


time_s = time.time()
sum = 1000

for a in range(1, sum):
    for b in range(a + 1, sum):
        c = b + 1
        while c * c < b * b + a + a:
            c += 1
        if a + b + c == 1000 and c ** 2 == a ** 2 + b ** 2 and c <= sum:
            print("Product: ", a * b * c)

time_f = time.time() - time_s
print("Time: ", time_f)

time_s = time.time()
sum = 1000

for a in range(1, sum):
    for b in range(a + 1, sum):
        for c in range(b + 1, sum):
            if is_triple(a, b, c) and a + b + c == 1000:
                print(a, b, c)
                print(a * b * c)

time_f = time.time() - time_s
print("Time: ", time.time())

time_s = time.time()
sum = 1000

for a in range(1, sum):
    for b in range(1, sum):
        for c in range(1, sum):
            if is_triple(a, b, c) and a + b + c == 1000:
                print(a, b, c)
                print(a * b * c)

time_f = time.time() - time_s
print("Time: ", time)
