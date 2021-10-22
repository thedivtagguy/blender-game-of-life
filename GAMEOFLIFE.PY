import random as random
import mathutils
# Generate a sequence of even numbers
def even_seq(n):
    grid = []
    for j in range(0,n*2):
        if j % 2 == 0:
            grid.append(j)
    return grid
    
def generate_grid(a):
    x = a
    y = a
    z = a
    grid = {}
    numbers = even_seq(x)
    for i in range(0,x):
        b = numbers[i]
        for j in range(0,y):
            a = numbers[j]
            for k in range(0,z):
                c = numbers[k]
            # Add new cell to the grid
                grid[(a,b,c)] = True

    return grid


grid = generate_grid(3)


def get_neighbors(grid, x,y,z):
    count = 0
    for pos in (
        (x-2,y-2,z-2),
        (x-2,y-2,z),
        (x-2,y-2,z+2),
        (x-2,y,z-2),
        (x-2,y,z),
        (x-2,y,z+2),
        (x-2,y+2,z-2),
        (x-2,y+2,z),
        (x-2,y+2,z+2),
        (x,y-2,z-2),
        (x,y-2,z),
        (x,y-2,z+2),
        (x,y,z-2),
        (x,y,z+2),
        (x,y+2,z-2),
        (x,y+2,z),
        (x,y+2,z+2),
        (x+2,y-2,z-2),
        (x+2,y-2,z),
        (x+2,y-2,z+2),
        (x+2,y,z-2),
        (x+2,y,z),
        (x+2,y,z+2),
        (x+2,y+2,z-2),
        (x+2,y+2,z),
        (x+2,y+2,z+2)):
        if pos in grid:
            if grid[pos] == True:
                count += 1
    return count


# Function to determine if cell is alive or dead
def is_alive(grid, x,y,z):
    if (x,y,z) in grid:
        if grid[(x,y,z)] == True:
            return True
    return False

# Function to calculate next iteration
def next_iteration(grid):
    new_grid = {}
    for x in range(0,len(grid)):
        for y in range(0,len(grid)):
            for z in range(0,len(grid)):
                neighbors = get_neighbors(grid, x,y,z)
                if is_alive(grid, x,y,z):
                    if neighbors < 2:
                        new_grid[(x,y,z)] = False
                    elif neighbors > 3:
                        new_grid[(x,y,z)] = False
                    else:
                        new_grid[(x,y,z)] = True
                else:
                    if neighbors == 3:
                        new_grid[(x,y,z)] = True
                    else:
                        new_grid[(x,y,z)] = False
    return new_grid
# Function to initiate N number of iterations and return the final grid
def iterate(grid, n):
    for i in range(0,n):
        grid = next_iteration(grid)
    return grid
iterate(grid, 1)