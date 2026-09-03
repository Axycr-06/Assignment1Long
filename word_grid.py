import random
import string

def init():
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)

    return grid_size

def make_grid(grid_size):
    grid = []

    for i in range(grid_size):
        #create empty row first so that it can be filled
        row = []

        #loop through the grid size to create the columns
        for t in range(grid_size):
            #append a random letter to the row
            row.append(random.choice(string.ascii_lowercase))

        #add the row to the grid
        grid.append(row)

    return grid

def print_grid(grid):
    for row in grid:
        print(",".join(row))

print_grid(make_grid(init()))