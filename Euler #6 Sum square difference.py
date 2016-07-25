import time


def sum_square_difference(number):
    time_1 = time.time()
    square_sum = 0
    sum = 0
    for x in range(number + 1):
        square_sum += x ** 2
        sum += x

    squared = sum ** 2
    difference = abs(square_sum - squared)

    time_2 = time.time()
    print("\nTime: ", str((time_2 - time_1) * 1000000), "ms")

    print("Sum of the squares: " + str(square_sum))
    print("\nSum of one hundred natural numbers: " + str(sum))
    print("Squared sum: " + str(squared))
    print("\nDifference between the sums: " + str(difference))

    time_3 = time.time()
    square_sum = ((number * (number + 1) * ((2 * number) + 1))) / 6
    sum = (number * (number + 1)) / 2
    # for x in range (number+1):
    #    square_sum += x**2


    squared = sum ** 2
    difference = abs(square_sum - squared)

    time_4 = time.time()
    print("\nTime: ", str((time_4 - time_3) * 1000000), "ms")

    print("Sum of the squares: " + str(square_sum))
    print("\nSum of one hundred natural numbers: " + str(sum))
    print("Squared sum: " + str(squared))
    print("\nDifference between the sums: " + str(difference))
