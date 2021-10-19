import random as random
# Generate a sequence of even numbers
def even_seq(n):
    grid = []
    for j in range(0,n*2):
        if j % 2 == 0:
            grid.append(j)
    return grid


# Grid to plot locations of the points on the 
# user defined grid without overlap.
def generate_grid(a):
    x = a
    y = a
    grid = []
    numbers = even_seq(x)
    for i in range(0,x):
        b = numbers[i]
        for j in range(0,y):
            a = numbers[j]
            new_loc = [a,b,0]
            grid.append(new_loc)

    return grid

# function to delete random item from grid
def delete_random_item(grid, x):
    b = grid
    a = len(b) -1
    # Get random index
    for x in range(0,x):
        random_index = random.randint(0,(a-1))
        # Delete item from grid
        b.pop(random_index)
    return b