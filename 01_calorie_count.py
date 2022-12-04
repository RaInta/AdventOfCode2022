from typing import List
from pathlib import Path

DATA_PATH = Path().cwd() / "data"

# For testing: use 01_test_input.txt
with (DATA_PATH / "01_input.txt").open() as f1:
    calories = f1.read().splitlines()
    # Because I'm lazy and don't want to worry about the last item edge-case
    calories.append('')


def parse_input(calory_list: List[str]) -> List[int]:
    caloric_total = []
    item_total = 0
    for item in calory_list:
        if not len(item):
            caloric_total.append(item_total)
            item_total = 0
        else:
            item_total += int(item)
    return caloric_total


caloric_total = parse_input(calories)

print(f"The maximum total calories any single elf is carrying is {max(caloric_total):,} calories.")

# Solution for part two
caloric_total.sort(reverse=True)

print(f"The total calories carried by the top three Elves is {sum(caloric_total[:3]):,} calories.")