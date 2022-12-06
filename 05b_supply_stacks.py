from typing import List, Tuple
from pathlib import Path
import re

DATA_PATH = Path().cwd() / "data"


def parse_input(filename: str, data_path: Path=DATA_PATH) -> Tuple[List[List[str]], Tuple[int, int, int]]:
    with (data_path / filename).open() as f1:
        crates_input = f1.read()

    # Initial parse; split between crate state and instructions
    [crates_raw, instructions_raw] = re.split(r"\s+" + r"\s+".join((str(x) for x in range(1, 4))), crates_input)
    crate_list = crates_raw.splitlines()
    crate_list.reverse()

    # Generate list of lists
    L = len(crate_list[0])
    splits = range(3, L + 1, 4)
    all_crates = [list() for __ in range(len(splits))]
    for crate in crate_list:
        crate = re.sub(r"^", "  ", crate)
        for idx, present_idx in enumerate(splits):
            all_crates[idx].append(crate[present_idx] )

    # Clean up spaces
    for crate_list in all_crates:
        for __ in range(crate_list.count(' ')):
            crate_list.remove(' ')

    # Parse instructions
    instructions_list = instructions_raw.splitlines()
    instructions_list = instructions_list[2:]
    instructions = []
    for instruction in instructions_list:
        instructions.append([int(x) for x in re.findall(r'\d+', instruction)])

    return all_crates, instructions


def move_crate(crate_state: List[List[str]], instruction: List[int]):
    crate_state_new = crate_state.copy()
    [move, crate_from, crate_to] = instruction
    # print(f"Moving {crate_state_new[crate_from - 1][-move:]}")
    crate_state_new[crate_to - 1].extend(crate_state_new[crate_from - 1][-move:])
    crate_state_new[crate_from - 1] = crate_state_new[crate_from - 1][:-move]
    return crate_state_new


def get_end_crates(crate_state: List[List[str]], instructions: List[List[int]]) -> str:
    for instruction in instructions:
        crate_state = move_crate(crate_state, instruction)
    return  "".join([crate[-1] for crate in crate_state])


# crates, instructions = parse_input("05_test_input.txt")
crates, instructions = parse_input("05_input.txt")

print(f"Top crates: {get_end_crates(crates, instructions)}")

crates = move_crate(crates, instructions[0])
crates = move_crate(crates, instructions[1])
crates = move_crate(crates, instructions[2])
crates
