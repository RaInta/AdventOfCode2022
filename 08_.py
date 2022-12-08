from typing import List, Tuple
from pathlib import Path

DATA_PATH = Path().cwd() / "data"


def parse_input(filename: str, data_path: Path=DATA_PATH) -> List[List[str]]:
    with (data_path / filename).open() as f1:
        games = f1.read().splitlines()
    games = [x.split() for x in games]
    return games


def get_total_score(games: List[str]) -> int:
    pass


games = parse_input("08_test_input.txt")
# games = parse_input("08_input.txt")


print(f"Total score: {get_total_score(games):,}")
