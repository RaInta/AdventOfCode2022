from typing import List, Tuple
from pathlib import Path
from numpy import array
import numpy as np

DATA_PATH = Path().cwd() / "data"


def parse_input(filename: str, data_path: Path=DATA_PATH) -> List[List[str]]:
    with (data_path / filename).open() as f1:
        grid = f1.read().splitlines()
    grid = [list(x) for x in grid]
    return array(grid).astype("int")


def is_visible(x: int, y: int, grid: array) -> bool:
    val = grid[y, x]
    if (x == 0) or (y == 0) or (x == grid.shape[0]) or (y == grid.shape[1]):
        return True
    else:
        return (grid[:y, x] < val).all() or (grid[y+1:, x] < val).all() or (grid[y, :x] < val).all() or (grid[y, x+1:] < val).all()


def get_visibility_score(x: int, y: int, grid: array) -> int:
    val = grid[y, x]
    a1 = grid[:y, x][::-1] < val
    a2 = grid[y+1:, x] < val
    a3 = grid[y, :x][::-1] < val
    a4 = grid[y, x+1:] < val
    if (y != 0) or (y != grid.shape[0]):
        a1[-1] = False
        a2[-1] = False
    if (x != 0) or (x != grid.shape[1]):
        a3[-1] = False
        a4[-1] = False
    v1 = np.argmin(a1) + 1
    v2 = np.argmin(a2) + 1
    v3 = np.argmin(a3) + 1
    v4 = np.argmin(a4) + 1
    return v1 * v2 * v3 * v4


def get_max_visibility(grid: array) -> int:
    max_visibility = 1
    # If you're using for-loops with NumPy, you're doing something wrong...
    # Especially a double for-loop
    # Brutally excoriate the edge cases!
    for row in range(1, grid.shape[0] - 1):
        for col in range(1, grid.shape[1] - 1):
            visibility = get_visibility_score(row, col, grid)
            if visibility > max_visibility:
                max_visibility = visibility
    return max_visibility

# grid = parse_input("08_test_input.txt")
grid = parse_input("08_input.txt")

print(f"Maximum visibility : {get_max_visibility(grid):,}")

get_max_visibility(grid)