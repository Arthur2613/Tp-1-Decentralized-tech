import os
import time

def clear_screen():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid(rows, cols):
    """Create an empty grid with given rows and columns."""
    return [[0 for _ in range(cols)] for _ in range(rows)]

def print_grid(grid):
    """Display the grid in the console."""
    for row in grid:
        print(''.join('#' if cell else ' ' for cell in row))

def count_neighbors(grid, row, col):
    """Count the live neighbors of a cell."""
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),
        (0, -1),          (0, 1),
        (1, -1), (1, 0), (1, 1)
    ]
    count = 0
    for dr, dc in neighbors:
        r, c = row + dr, col + dc
        if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
            count += grid[r][c]
    return count

def next_generation(grid):
    """Calculate the next generation of the grid."""
    rows, cols = len(grid), len(grid[0])
    new_grid = create_grid(rows, cols)

    for row in range(rows):
        for col in range(cols):
            live_neighbors = count_neighbors(grid, row, col)

            if grid[row][col] == 1:
                if live_neighbors in [2, 3]:
                    new_grid[row][col] = 1
            else:
                if live_neighbors == 3:
                    new_grid[row][col] = 1

    return new_grid

def main():
    rows, cols = 20, 40
    grid = create_grid(rows, cols)

    # Initialize with a simple pattern (e.g., a glider)
    grid[1][2] = 1
    grid[2][3] = 1
    grid[3][1] = 1
    grid[3][2] = 1
    grid[3][3] = 1

    try:
        while True:
            clear_screen()
            print_grid(grid)
            grid = next_generation(grid)
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("\nGame terminated.")

if __name__ == "__main__":
    main()
