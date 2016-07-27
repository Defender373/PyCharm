# RPI2020

# Idea, build functions to calculate the product in each of the 8 directions, I've done up and left

#call up on Euler[10][11], up(Euler, 10, 11)
#call left on Euler[10][11], left(Euler[10], 11)
import time


def up(array, column_index, row_index):
    return array[row_index][column_index] * array[row_index - 1][column_index] * array[row_index - 2][column_index] * \
           array[row_index - 3][column_index]


def down(array, column_index, row_index):
    return array[row_index][column_index] * array[row_index + 1][column_index] * array[row_index + 2][column_index] * \
           array[row_index + 3][column_index]


def left(row_array, column_index):
    return row_array[column_index] * row_array[column_index - 1] * row_array[column_index - 2] * row_array[
        column_index - 3]


def right(row_array, column_index):
    return row_array[column_index] * row_array[column_index + 1] * row_array[column_index + 2] * row_array[
        column_index + 3]


def up_left(array, column_index, row_index):
    return array[row_index][column_index] * array[row_index - 1][column_index - 1] * array[row_index - 2][
        column_index - 2] * \
           array[row_index - 3][column_index - 3]


def up_right(array, column_index, row_index):
    return array[row_index][column_index] * array[row_index - 1][column_index + 1] * \
           array[row_index - 2][column_index + 2] * array[row_index - 3][column_index + 3]


def down_left(array, column_index, row_index):
    return array[row_index][column_index] * array[row_index - 1][column_index - 1] * \
           array[row_index - 2][column_index - 2] * array[row_index - 3][column_index - 3]


def down_right(array, column_index, row_index):
    return array[row_index][column_index] * array[row_index + 1][column_index - 1] * \
           array[row_index + 2][column_index - 2] * array[row_index + 3][column_index - 3]


start_time = time.time()

Euler = [[-1] * 20 for x in range(20)]

Euler[15][12] = 20
# print(Euler[][12])
f = open('Euler11numbers.txt', 'r')

# f.readline()[4] gets the character at index 4 in the line that was just read

# ALGORITHM
# for x in range 20 to get each line, which represents a row in the 2x2 array
for y in range(20):
    line = f.readline()
    # for y in range(0,20,3) counts from 0 to 20 by 3's allowing us to skip spaces
    for x in range(0, 60, 3):
        # Euler[x][y] = substring y to y+1 cast to an int; int()
        Euler[y][int(x / 3)] = int(line[x:x + 2])


max = 0
print("Hi")
tester = 0
for y in range(20):
    for x in range(20):
        if (x >= 3):
            tester = left(Euler[y], x)
            if (tester > max):
                max = tester

        if (x <= 16):
            tester = right(Euler[y], x)
            if (tester > max):
                max = tester

        if (y >= 3):
            tester = up(Euler, x, y)
            if (tester > max):
                max = tester

        if (y <= 16):
            tester = down(Euler, x, y)
            if (tester > max):
                max = tester

        if (x >= 3 and y >= 3):
            tester = up_left(Euler, x, y)
            if (tester > max):
                max = tester

        if (y >= 3 and x <= 16):
            tester = up_right(Euler, x, y)
            if (tester > max):
                max = tester

        if (y <= 16 and x >= 3):
            tester = down_left(Euler, x, y)
            if (tester > max):
                max = tester

        if (x <= 15 and y <= 16):
            tester = down_right(Euler, x, y)
            if (tester > max):
                max = tester

print(max, '\n', (time.time() - start_time) * 1000)

for y in range(20):
    for x in range(20):

        if (x <= 16):
            tester = right(Euler[y], x)
            if (tester > max):
                max = tester

        if (y <= 16):
            tester = down(Euler, x, y)
            if (tester > max):
                max = tester

        if (y >= 3 and x <= 16):
            tester = up_right(Euler, x, y)
            if (tester > max):
                max = tester

        if (x <= 15 and y <= 16):
            tester = down_right(Euler, x, y)
            if (tester > max):
                max = tester
