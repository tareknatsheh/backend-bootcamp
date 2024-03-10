"""
Contains all the simulation logic
run() function takes the original initial state of the cells on the grid, and
returns the new state after running the simulation logic
"""

def run(the_grid: list[list]) -> list[list]:
    # Since lists are mutable, and we don't want to loose the initial state
    #  therefore, we would need to do a copy of the original

    # First let's initialize the new grid list
    new_grid = []
    for _ in range(len(the_grid)):
        new_grid.append([])

    # Go over the cells in the grid one by one and check if we have a living or dead cell
    # and check the number of adjacent neighbors
    for row_index, row in enumerate(the_grid):
        for col_index, cell in enumerate(row):
            neighbors = get_how_many_neighbors(the_grid, cell, row_index, col_index)
            # this function modifies the new_grid directly (because it's mutable)
            set_cell_new_state(new_grid, cell,  row_index, neighbors)
    return new_grid

def get_checking_range(col_index, lower, upper):
    """ returns the range making sure that it stays within upper and lower bounds """
    start = col_index - 1
    end = col_index + 1
    start = bound(start, lower, upper)
    end = bound(end, lower, upper)
    return start, end

def bound(x, lower, upper):
    """ force the lower and upper bounds """
    if x < lower:
        x = lower
    elif x > upper:
        x = upper
    return x

def get_how_many_neighbors(the_grid, cell, row_index, col_index):
    """ Check the square around our cell of interest """
    neighbors = 0
    row = the_grid[row_index]
    start, end = get_checking_range(col_index, 0, len(row) - 1)

    # if there is a row above it, check it.
    if row_index > 0:
        row_above = the_grid[row_index - 1]
        neighbors += row_above[start:end + 1].count("X")
    # check the same row
    neighbors += row[start:end + 1].count("X")
    if cell == "X":
        neighbors -= 1 # don't count yourself
    # if there is a row below it, check it.
    if row_index < (len(row) - 1):
        row_below = the_grid[row_index + 1]
        neighbors += row_below[start:end + 1].count("X")
    
    return neighbors

def set_cell_new_state(new_grid, cell, row_index, neighbors) -> None:
    """ Sets the new state of the target cell in the new grid """
    if cell == "X":
        if neighbors == 2 or neighbors == 3:
            new_grid[row_index].append("X")
        else:
            new_grid[row_index].append("_")
    else:
        if neighbors == 3:
            new_grid[row_index].append("X")
        else:
            new_grid[row_index].append("_")
