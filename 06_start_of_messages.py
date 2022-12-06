from typing import List, Tuple
from pathlib import Path

DATA_PATH = Path().cwd() / "data"


def parse_input(filename: str, data_path: Path=DATA_PATH) -> List[List[str]]:
    with (data_path / filename).open() as f1:
        input_str = f1.read()
    return input_str


def get_start_of_packet(input_str: str) -> int:
    for idx in range(len(input_str) - 3):
        if len(input_str[idx:idx + 4]) == len(set(input_str[idx:idx + 4])):
            break
    return idx + 4


def get_start_of_message(input_str: str) -> int:
    for idx in range(len(input_str) - 13):
        if len(input_str[idx:idx + 14]) == len(set(input_str[idx:idx + 14])):
            break
    return idx + 14


test_str = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"  # 7 (part 1), 19 (part 2)
test_str = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"  # 11 (part 1), 26 (part 2)

get_start_of_message(test_str)

input_str = parse_input("06_input.txt")

print(f"Start of packet index: {get_start_of_packet(input_str)}")
print(f"Start of message index: {get_start_of_message(input_str)}")
