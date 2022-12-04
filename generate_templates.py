# Generate template Python scripts and empty text file 
# templates for each day of the Advent of Code
from shutil import copy as fcopy
from pathlib import Path

base_dir = Path.cwd() / "templates2"
base_dir.mkdir(parents=True, exist_ok=True)

for num in range(2, 26):
    fcopy("00_template.py", base_dir / f"{num:02}_.py")
    fcopy("00_template.py", base_dir / f"{num:02}b_.py")
    (base_dir / f"{num:02}_input.txt").touch()
    (base_dir / f"{num:02}_test_input.txt").touch()