"""
This file is responsible for all logging, to the CLI and to folders
It also handles user input
"""

def print_grid(grid_matrix: list[list]) -> None:
    """
    Prints the updated grid to the console
    """
    # First, print the columns numbers
    for col_ind in range(len(grid_matrix)):
        if col_ind == 0:
            print("  " + str(col_ind), end="")
        else:
            print(" " + str(col_ind), end="")

    # Make a new line and print the cell number and the cell content:
    print("")
    for row_ind, row in enumerate(grid_matrix):
        print(str(row_ind) + "|", end="")
        for cell in row:
            print(cell + "|", end="")
        print("")
    pass


def ask_user_to_add_cells(grid_size) -> list:
    """It get's the user input then after finishing it returns a list of tuples
    Example: [(0, 0), (5, 3), (2, 1)]
    means that the user wants three cells, the first cell would be at row 0 col 0 in our grid
    the second cell will be at row 5 col 3 ,... and so on
    """
    cells_to_add_list = []

    print("Let's add some living cells.\ninput the row and column number of the cells you wish to create separated by a space.")
    print("Example: 0 3\nThis would add a new cell at row 0 column 3 of our grid")
    take_input = True
    while take_input:
        # Let user initialize the grid with living cells
        user_input = input("Row and column (keep empty and press enter when finished):").split()
        if isinstance(user_input, list) and len(user_input) == 2:
            row, col = user_input
            row = int(row)
            col = int(col)
            if row < 0 or row > (grid_size - 1) or col < 0 or col > (grid_size - 1):
                raise Exception(f"Row and column should be between 0 and {(grid_size - 1)}")
            cells_to_add_list.append((row, col))
        else:
            take_input = False
    
    return cells_to_add_list

def ask_user_how_many_rounds() -> int:
    """ Takes and validates the required number of rounds to run the simulation """
    user_input = int(input("How many rounds?\n"))
    if user_input < 2 or user_input > 100:
        raise Exception("Wrong input, number of round should be between 2 and 100")
    return user_input

def what_grid_size() -> int:
    """ Takes and validates the size of the grid """
    user_input = input("What is the grid size?\n")
    user_input = int(user_input)
    if user_input < 2 or user_input > 10:
        raise Exception("Grid size must be only between 2x2 to 10x10")
    
    return user_input