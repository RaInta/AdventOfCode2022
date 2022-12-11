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

def get_total_visible(grid: array) -> int:
    total_visible = 0
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            total_visible += is_visible(row, col, grid=grid)
    return total_visible


# grid = parse_input("08_test_input.txt")
grid = parse_input("08_input.txt")

print(f"Total visible trees: {get_total_visible(grid):,}")

get_total_visible(grid)
