from string import ascii_letters
from typing import List, Set
from pathlib import Path

DATA_PATH = Path().cwd() / "data"


def parse_input(filename: str, data_path: Path=DATA_PATH) -> List[List[str]]:
    items = []
    with (data_path / filename).open() as f1:
        raw_items = f1.read().splitlines()
    group = []
    for idx, item in enumerate(raw_items, start=1):
        group.append(item)
        if not idx%3:
            items.append(group)
            group = []
    return items


def get_common_elements(a: str, b: str, c: str) -> str:
    """Get common characters between two sets of strings.

    Args:
        a (str): Input string of characters 
        b (str): Input string of characters 
        c (str): Input string of characters 

    Returns:
        common (str): string of characters in common between a, b and c
    """
    common = set(b).intersection(set(a)).intersection(set(c))
    return "".join(common)


def get_priority(s: str) -> int:
    return ascii_letters.find(s) + 1


def get_total_priority(items: List[List[str]]) -> int:
    return sum([get_priority(get_common_elements(item[0], item[1], item[2])) for item in items])


# items = parse_input("03_test_input.txt")
items = parse_input("03_input.txt")

print(f"Sum of priorities: {get_total_priority(items):,}")

get_total_priority(items)