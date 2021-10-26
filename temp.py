def game_of_life(grid, i):
    next_grid = []
    for j in range(0,len(grid)):
        for i in range(0,len(grid)):
            for k in range(0,len(grid)):
                
                # Get the number of neighbors
                neighbors = get_neighbors(grid, i, j)
                # Get the current state of the cell
                current_state = grid[i][j]
                # Get the next state of the cell
                next_state = get_next_state(current_state, neighbors)
                # Append the next state to the next grid
                next_grid.append(next_state)


        neighbors = 0
        for k in range(0,len(grid)):
            if grid[j][0] == grid[k][0] and grid[j][1] == grid[k][1] and grid[j][2] == grid[k][2]:
                if grid[j][3] == True:
                    neighbors += 1
        # Check if the current location is alive
        if grid[j][3] == True:
            if neighbors == 2 or neighbors == 3:
                grid[j][3] = True
                next_grid.append(grid[j])
        else: 
            if neighbors == 3:         
                if grid[j][3] == False:
                # If it has 3 neighbors, add the location to the next grid
                  grid[j][3] = True
                  next_grid.append(grid[j])
        else: 
            if grid[j][3] == True:
                grid[j][3] = False
                next_grid.append(grid[j])

                
   
    return next_grid

def get_neighbors(grid):
    # Calculating Moore Neighbours in 3D Space
    neighbors = 0
    # Cube root grid
    n = int(len(grid)**(1/3))
    # Get the current location
    i = grid[0]
    # Get the neighbors
    if i > 0:
        if j > 0:
            if k > 0:
                if grid[i-1][j-1][k-1] == True:
                    neighbors += 1
            if k < n:
                if grid[i-1][j-1][k+1] == True:
                    neighbors += 1
        if j < n:
            if k > 0:
                if grid[i-1][j+1][k-1] == True:
                    neighbors += 1
            if k < n:
                if grid[i-1][j+1][k+1] == True:
                    neighbors += 1
   
 
[[0, 0, 0, True], [0, 0, 2, True], [0, 0, 4, True], [0, 0, 6, True], 
 [2, 0, 0, True], [2, 0, 2, True], [2, 0, 4, True], [2, 0, 6, True], 
 [4, 0, 0, True], [4, 0, 2, True], [4, 0, 4, True], [4, 0, 6, True], 
 [6, 0, 0, True], [6, 0, 2, True], [6, 0, 4, True], [6, 0, 6, True], 

 [0, 2, 0, True], [0, 2, 2, True], [0, 2, 4, True], [0, 2, 6, True], 
 [2, 2, 0, True], [2, 2, 2, True], [2, 2, 4, True], [2, 2, 6, True], 
 [4, 2, 0, True], [4, 2, 2, True], [4, 2, 4, True], [4, 2, 6, True], 
 [6, 2, 0, True], [6, 2, 2, True], [6, 2, 4, True], [6, 2, 6, True], 

 [0, 4, 0, True], [0, 4, 2, True], [0, 4, 4, True], [0, 4, 6, True], 
 [2, 4, 0, True], [2, 4, 2, True], [2, 4, 4, True], [2, 4, 6, True], 
 [4, 4, 0, True], [4, 4, 2, True], [4, 4, 4, True], [4, 4, 6, True], 
 [6, 4, 0, True], [6, 4, 2, True], [6, 4, 4, True], [6, 4, 6, True], 

 [0, 6, 0, True], [0, 6, 2, True], [0, 6, 4, True], [0, 6, 6, True], 
 [2, 6, 0, True], [2, 6, 2, True], [2, 6, 4, True], [2, 6, 6, True], 
 [4, 6, 0, True], [4, 6, 2, True], [4, 6, 4, True], [4, 6, 6, True], 
 [6, 6, 0, True], [6, 6, 2, True], [6, 6, 4, True], [6, 6, 6, True]]