import random as random
import mathutils
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
    z = a
    grid = []
    numbers = even_seq(x)
    for i in range(0,x):
        b = numbers[i]
        for j in range(0,y):
            a = numbers[j]
            for k in range(0,z):
                c = numbers[k]
                new_loc = [a,b,c, True]
                grid.append(new_loc)

    return grid

# function to delete random item from grid
def delete_random_item(grid,x):
    y = 0
    while y < x:
        z = random.randint(0,len(grid)-1)
        # Make z index location False
        grid[z][3] = False
        # Pop item
        grid.pop(z)
        y += 1
    return grid


    # Function that takes in an object, finds the dimensions and returns the number of cubes that can fit inside it
def get_dimensions(obj):
    # Get the dimensions of the object
    dim_x = obj.dimensions.x
    dim_y = obj.dimensions.y
    dim_z = obj.dimensions.z
    
    # Volume of object
    vol = dim_x * dim_y * dim_z
    cube_size = 2
   
    # Number of cubes that can fit inside the object rounded down integer
    num_cubes = round(vol/(cube_size*cube_size*cube_size))
    # Cube root of the number of cubes
    cube_root = round(num_cubes**(1/3))

    return cube_root

def update_camera(camera, focus_point=mathutils.Vector((0.0, 0.0, 0.0)), distance=10.0):
    looking_direction = camera.location - focus_point
    rot_quat = looking_direction.to_track_quat('Z', 'Y')
    camera.rotation_euler = rot_quat.to_euler()
    camera.location = rot_quat @ mathutils.Vector((0.0, 0.0, distance))

