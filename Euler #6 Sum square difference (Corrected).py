def sum_square_difference(number):
    square_sum = ((number * (number + 1) * ((2 * number) + 1))) / 6
    sum = (number * (number + 1)) / 2
    # for x in range (number+1):
    #    square_sum += x**2


    squared = sum ** 2
    difference = abs(square_sum - squared)

    print("Sum of the squares: " + str(square_sum))
    print("\nSum of one hundred natural numbers: " + str(sum))
    print("Squared sum: " + str(squared))
    print("\nDifference between the sums: " + str(difference))
