import random as random
# Make a 3D array of locations
def create_grid(n):
    grid = []
    x = 0
    for i in range(n):
        buf = []
        for j in range(n):
            buf2 = []
            for k in range(n):
                buf2.append(False)
                x+=1
            buf.append(buf2)
        grid.append(buf)    
    return grid

def neighbor(grid, x,y,z):
    count = 0
    for i in range(-1,2):
        for j in range(-1,2):
            for k in range(-1,2):
                if (x+i,y+j,z+k) in grid:
                    if grid[(x+i,y+j,z+k)] == True:
                        count += 1
    return count

def next_state(previous):
    n = len(previous)
    next = create_grid(n)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                N = neighbor(grid,i,j,k)
                if previous[i][j][k] == True:
                    if N < 2:
                        next[i][j][k] = False
                    elif N > 3:
                        next[i][j][k] = False
                    else:
                        next[i][j][k] = True
                else:
                    if N == 3:
                        next[i][j][k] = True
                    else:
                        next[i][j][k] = False
    return next



# Randomly set grid items to True or False
def random_grid(grid):
    n = len(grid)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                grid[i][j][k] = random.choice([True,False])
    return grid

# Calculate iterations of game of life
def iterations(grid, n):
    for i in range(n):
        grid = next_state(grid)
    return grid

# Count number of items in grid that are True
def count_live_items(grid):
    n = len(grid)
    count = 0
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if grid[i][j][k] == True:
                    count += 1
    return count

grid = create_grid(3)
grid = random_grid(grid)
neighbor(grid,1,2,0)
grid = iterations(grid,2)


count_live_items(grid)