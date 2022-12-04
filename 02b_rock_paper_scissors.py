from typing import List, Tuple
from pathlib import Path

DATA_PATH = Path().cwd() / "data"


def parse_input(filename: str, data_path: Path=DATA_PATH) -> List[List[str]]:
    with (data_path / filename).open() as f1:
        games = f1.read().splitlines()
    games = [x.split() for x in games]
    return games


def game_result(a: str, b: str) -> int:
    """Get result of Rock, Paper, Scissors between players a and b.
    The inputs have been encoded as:
    A/X -> 0: Rock
    B/Y -> 1: Paper
    C/Z -> 2: Scissors

    This is an example of a non-transitive game. Hence the 
    relative win is represented as a ring cycle (in this case, as a ring: Z_3)

    Interpreting the result:
    0: Draw
    1: Player B wins
    2: Player B loses


    Args:
        a (int): Player A's move, encoded as {0, 1, 2}
        b (int): Player B's move, encoded as {0, 1, 2}

    Returns:
        int: Outcome of game {0, 1, 2} 
    """
    encoding_a = {y: x for (x, y) in enumerate("ABC")}
    encoding_b = {y: x for (x, y) in enumerate("XYZ")}

    return (encoding_b[b] - encoding_a[a]) % 3


def get_move_from_result(a: str, result: str) -> str:
    encoding_a = {y: x for (x, y) in enumerate("ABC")}
    encoding_result = {"X": 2, "Y": 0, "Z": 1}
    # The following is an inversion of the above modulo difference
    numerical_b = (encoding_result[result] + encoding_a[a]) % 3
    encoding_b_reverse = {x: y for (x, y) in enumerate("XYZ")}
    return encoding_b_reverse[numerical_b]


def score_result(a: str, b: str) -> int:
    # Anticipating possible decoupling of this encoding in the follow-up puzzle
    encoding_b = {y: x for (x, y) in enumerate("XYZ")}
    encoding_score = {0: 3, 1: 6, 2: 0}
    result = game_result(a, b)
    score = encoding_score[result] + encoding_b[b] + 1 
    return score


def get_total_score(games: List[List[str]]) -> int:
    scores = [score_result(game[0], get_move_from_result(game[0], game[1])) for game in games]
    return sum(scores) 


# games = parse_input("02_test_input.txt")
games = parse_input("02_input.txt")

print(f"Total score: {get_total_score(games):,}")

get_total_score(games)