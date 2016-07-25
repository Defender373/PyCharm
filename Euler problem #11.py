# RPI2020

Euler = [[-1] * 20 for x in range(20)]

Euler[15][12] = 20
print(Euler[15][12])
f = open('Euler11numbers.txt', 'r')

print(f.readline())
# f.readline()[4] gets the character at index 4 in the line that was just read

# ALGORITHM
# for x in range 20 to get each line, which represents a row in the 2x2 array

    # for y in range(0,20,3) counts from 0 to 20 by 3's allowing us to skip spaces

        # Euler[x][i] = substring i to i+1 cast to an int; int()
