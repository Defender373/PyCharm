# RPI2020

Euler = [[-1] * 20 for x in range(20)]

Euler[15][12] = 20
print(Euler[][12])
f = open('Euler11numbers.txt', 'r')

print(f.readline())
# f.readline()[4] gets the character at index 4 in the line that was just read

# ALGORITHM
# for x in range 20 to get each line, which represents a row in the 2x2 array

    # for y in range(0,20,3) counts from 0 to 20 by 3's allowing us to skip spaces

        # Euler[x][i] = substring i to i+1 cast to an int; int()

# Idea, build functions to calculate the product in each of the 8 directions, I've done up and left

#call up on Euler[10][11], up(Euler, 10, 11)
#call left on Euler[10][11], left(Euler[10], 11)

def up(self, array, x_index, y_index):
    return array[y_index][x_index]*array[y_index+1][x_index]*array[y_index+2][x_index]*array[y_index+3][x_index]

def down(self, array, x_index, y_index):
    product = 0

    return product

def left(self, array, x_index):
    return array[x_index]*array[x_index-1]*array[x_index-2]*array[x_index-3]

def right(self, array, x_index):
    product = 0

    return product

def up_left(self, array, x_index, y_index):
    product = 0

    return product

def up_right(self, array, x_index, y_index):
    product = 0

    return product

def down_left(self, array, x_index, y_index):
    product = 0

    return product

def down_right(self, array, x_index, y_index):
    product = 0

    return product