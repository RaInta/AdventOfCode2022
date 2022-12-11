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
    def __init__(self, name: str="/", parent=None, files=[], children={}) -> None:
        self.name = name
        self.parent = parent
        self.files = files 
        self.children = children

    def add_files(self, files=[]):
        self.files.extend(files)

    def add_children(self, child_names):
        children = {name: Directory(name=name, parent=self, files=[], children={}) for name in child_names}
        self.children.update(children)
    
    def dir_size(self):
        return sum([x[0] for x in self.files])
    
    def cd(self, command: str="/"):
        if command == "..":
            self = self.parent
        else:
            self = self.children[command]
    
    def ls(self, command: str):
         pass


def breadth_first_search(visit_complete, graph, current_node):
    output = []
    visit_complete.append(current_node)
    queue = [current_node]
 
    while queue:
        s = queue.pop(0)
        output += s
 
        for neighbour in graph[s]:
            if neighbour not in visit_complete:
                visit_complete.append(neighbour)
                queue.append(neighbour)
    return output, visit_complete
 

root_dir = Directory(name="/", parent=None)
root_dir.add_files([(14848514, "b.txt"), (8504156,"c.dat")])
root_dir.add_children(["a", "b"])
root_dir.children["a"].add_files([(54689, "sfd.txt"), (89097, "beef.dat")])
root_dir.children["b"].add_files([(66665, "hyt.txt"), (3242, "nonono.exe")])
root_dir.children["a"].add_children("c")
root_dir.children["a"].children["c"].add_files([(8979, "end.txt")])
root_dir.children["b"].add_children("d")

print(root_dir.children["a"].children["c"].files)
root_dir.children["a"].children["c"].children == {}

while root_dir.children != {}:
    for child_name in root_dir.children:
        child = root_dir.children[child_name]
        print("directory: ", child.name)
        print("size:", child.dir_size())
    root_dir = child 


while root_dir.children is not None:
    for child_name in root_dir.children:
        child = root_dir.children[child_name]
        print(child.name)
        print(child.dir_size())
    root_dir = child


print(root_dir.children)

root_dir.dir_size()



def get_total_size(commands: List[str]) -> int:
    pass


commands = parse_input("07_test_input.txt")
# commands = parse_input("07_input.txt")


print(f"Total sizes of directories, where each size < 100,000: {get_total_size(commands):,}")
