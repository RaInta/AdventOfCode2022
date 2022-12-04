from typing import List, Tuple
from pathlib import Path

DATA_PATH = Path().cwd() / "data"


def parse_input(filename: str, data_path: Path=DATA_PATH) -> List[List[str]]:
    with (data_path / filename).open() as f1:
        raw_pairs = f1.read().splitlines()
    pairs = []
    for pair in raw_pairs:
        [pair1, pair2] = pair.split(",")
        pairs.append([[int(x) for x in pair1.split("-")], [int(x) for x in pair2.split("-")]])
    return pairs 


def is_completely_overlapping(a: List[int], b: List[int]) -> bool:
    set_a = set(range(a[0], a[1] + 1))
    set_b = set(range(b[0], b[1] + 1))
    return set_a.issubset(set_b) or set_b.issubset(set_a)


def is_overlapping(a: List[int], b: List[int]) -> bool:
    set_a = set(range(a[0], a[1] + 1))
    set_b = set(range(b[0], b[1] + 1))
    return len(set_a.intersection(set_b)) > 0


def get_total_overlapping(pairs: List[List[int]]) -> int:
    return sum([is_overlapping(x, y) for [x, y] in pairs])


# pairs = parse_input("04_test_input.txt")
pairs = parse_input("04_input.txt")

get_total_overlapping(pairs)

print(f"Total overlapping pairs: {get_total_overlapping(pairs):,}")