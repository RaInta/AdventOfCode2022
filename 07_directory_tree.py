from typing import List, Tuple
from pathlib import Path

DATA_PATH = Path().cwd() / "data"

# Find all of the directories with a total size of at most 100000. 
# What is the sum of the total sizes of those directories?

# Test example: directories are a and e; the sum of their total sizes is 95437 (94853 + 584). 
# (As in this example, this process can count files more than once!)

def parse_input(filename: str, data_path: Path=DATA_PATH) -> List[str]:
    with (data_path / filename).open() as f1:
        commands = f1.read().splitlines()
    commands = [x.split() for x in commands]
    return commands


class Directory():
    def __init__(self, name: str="/", parent=None, contents=[]) -> None:
        self.name = name
        self.parent = parent
        self.contents = contents

    def add_contents(self, contents=[]):
        self.contents.append(contents)


root_dir = Directory(name="/", parent=None)

root_dir.contents

root_dir.add_contents([Directory(name="a", parent=root_dir), (14848514, "b.txt"), (8504156,"c.dat"), Directory(name="d", parent=root_dir)])

root_dir.contents[0][0].name

, contents=[Directory(name="a", parent=dir1), (14848514, "b.txt"), (8504156,"c.dat"), Directory(name="d", parent=dir1)])

def get_total_score(games: List[str]) -> int:
    pass


games = parse_input("07_test_input.txt")
# games = parse_input("07_input.txt")


print(f"Total score: {get_total_score(games):,}")
