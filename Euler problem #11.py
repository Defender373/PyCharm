# RPI2020

Euler = [[-1] * 20 for x in range(20)]

Euler[15][12] = 20
#print(Euler[][12])
f = open('Euler11numbers.txt', 'r')


# f.readline()[4] gets the character at index 4 in the line that was just read

# ALGORITHM
# for x in range 20 to get each line, which represents a row in the 2x2 array
for x in range(20):
    line = f.readline()
    # for y in range(0,20,3) counts from 0 to 20 by 3's allowing us to skip spaces
    for y in range(0, 60, 3):
        # Euler[x][y] = substring y to y+1 cast to an int; int()
        print(line[y:y + 2])
        Euler[x][int(y / 3)] = int(line[y:y + 2])

print("test")


# Idea, build functions to calculate the product in each of the 8 directions, I've done up and left

#call up on Euler[10][11], up(Euler, 10, 11)
#call left on Euler[10][11], left(Euler[10], 11)

def up(self, array, column_index, row_index):
    return array[row_index][column_index] * array[row_index + 1][column_index] * array[row_index + 2][column_index] * \
           array[row_index + 3][column_index]


def down(self, array, column_index, row_index):
    product = 0

    return product


def left(self, array, column_index):
    return array[column_index] * array[column_index - 1] * array[column_index - 2] * array[column_index - 3]


def right(self, array, column_index):
    product = 0

    return product


def up_left(self, array, column_index, row_index):
    product = 0

    return product


def up_right(self, array, column_index, row_index):
    product = 0

    return product


def down_left(self, array, column_index, row_index):
    product = 0

    return product


def down_right(self, array, column_index, row_index):
    product = 0

    return product