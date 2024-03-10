"""
Game of life

It starts by letting the user decide where there is life in a nxn grid
And for how many rounds they want the simlulation to run.
Then the game runs the simulations round by round showing the result of each.

TODO:
finish block diagram

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

    # Print the user's initial grid:
    log.print_grid(our_grid)

    # Start the simulation!
    for round in range(num_of_rounds):
        print(f"Round: {round}")
        # Keep updating the grid with the new state coming from the simulation:
        our_grid = sim.run(our_grid)
        log.print_grid(our_grid)



if __name__ == "__main__":
    main()