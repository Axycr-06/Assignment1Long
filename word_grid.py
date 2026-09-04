"""
    File: word_grid.py
    Author: Shane Dyke
    Course: CSC 120, Fall 2026
    Purpose: This program takes two inputs; size of grid, and random_seed
    it then creates a grid of random letters
"""

import random
import string

def init():
    grid_size = int(input())
    seed_value = input()
    random.seed(seed_value)

    return grid_size

def make_grid(grid_size):
    grid = []

    #create empty row first so that it can be filled
    for i in range(grid_size):
        row = []

        #loop through the grid size to create the columns
        for t in range(grid_size):
            row.append(random.choice(string.ascii_lowercase)) #append a random letter to the row

       
        grid.append(row) #add the row to the grid

    return grid

def print_grid(grid):
    for row in grid:
        print(",".join(row)) #add a comma between each letter

print_grid(make_grid(init()))