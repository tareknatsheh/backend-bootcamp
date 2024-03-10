"""
Game of life

It starts by letting the user decide where there is life in a 8x8 grid
And for how many rounds they want the simlulation to run.
Then the game runs the simulations round by round showing the result of each.

"""

from utilities import logger as log, grid, simulator as sim

def main():
    """
    This is the start point of our game
    """

    # Ask the user what size they want the grid to be:
    grid_size = log.what_grid_size()
    # Generate it:
    our_grid = grid.generate_empty_grid(grid_size)
    # Print it:
    log.print_grid(our_grid)

    cells_to_add_list = log.ask_user_to_add_cells(grid_size)
    grid.add_cells(our_grid, cells_to_add_list)

    num_of_rounds = log.ask_user_how_many_rounds()

    
    log.print_grid(our_grid)

    # Start the simulation!
    sim.run(our_grid, num_of_rounds)

    pass


if __name__ == "__main__":
    main()