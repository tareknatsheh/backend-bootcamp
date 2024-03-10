def run(the_grid: list[list]) -> list[list]:
    # Since lists are mutable, therefore, we would need to do a copy of the original
    new_grid = []
    for _ in range(len(the_grid)):
        new_grid.append([])

    for row_index, row in enumerate(the_grid):
        for col_index, cell in enumerate(row):
            neighbors = 0
            start, end = get_checking_range(col_index, 0, len(row) - 1)
            if row_index > 0:
                # check the row above
                row_above = the_grid[row_index - 1]
                neighbors += row_above[start:end + 1].count("X")
            # check the same row
            neighbors += row[start:end + 1].count("X")
            if cell == "X":
                neighbors -= 1 # don't count yourself
            # check the row below it
            if row_index < (len(row) - 1):
                row_below = the_grid[row_index + 1]
                neighbors += row_below[start:end + 1].count("X")
            
            # print(f"Total for {row_index}{col_index} = {neighbors}")
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
    
    return new_grid

def get_checking_range(col_index, lb, ub):
    start = col_index - 1
    end = col_index + 1
    start = bound(start, lb, ub)
    end = bound(end, lb, ub)
    return start, end

    
def bound(x, lower, upper):
    if x < lower:
        x = lower
    elif x > upper:
        x = upper
    return x