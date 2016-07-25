def ndigits(x):
    if ((x ** 2) ** .5 < 1):
        return 0
    else:
        print(x / 10)
        return 1 + ndigits(x / 10)


print(ndigits(-9961434))
