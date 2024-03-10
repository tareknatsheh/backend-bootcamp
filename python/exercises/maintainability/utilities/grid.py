"""
Functionality relavent to our game grid
"""

def generate_empty_grid(n: int) -> list[list]:
    """ n is the grid dimensions (nXn) """
    result = []
    for _ in range(n):
        row = []
        for _ in range(n):
            row.append("_")
        result.append(row)
    return result

def add_cells(grid: list[list], cells_list: list[tuple]):
    pass