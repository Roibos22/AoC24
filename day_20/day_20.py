import sys
from collections import deque

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def print_map(map):
    for row in map:
        wide_chars = [str(char).center(3) if char != "'" else "   " for char in row]
        print(''.join(wide_chars))

def in_range(x, y, map):
    return (
        x >= 0 and\
        y >= 0 and\
        x < len(map[0]) and\
        y < len(map)
    )

def get_start(map):
    for row in range(len(map)):
        for col in range(len(map[row])):
            if map[row][col] == 'S':
                return (col, row)
    return (0, 0)

def bfs(map, start):
    dq = deque([(start, [start])])
    visited = {start}

    while dq:
        pos, path = dq.popleft()
        if map[pos[1]][pos[0]] == 'E':
            for i, p in enumerate(path):
                map[p[1]][p[0]] = str(i)
            return path

        for dx, dy in dirs:
            next = (pos[0] + dx, pos[1] + dy)
            if in_range(next[1], next[0], map) and map[next[1]][next[0]] != '#' and next not in visited:
                visited.add(next)
                dq.append((next, path + [next]))

    print(dq)

def find_targets_in_range(pos, delay, map, targets=None):
    if targets is None: targets = set()
    if delay <= 0: return targets

    for dx, dy in dirs:
        next = (pos[0] + dx, pos[1] + dy)
        if in_range(next[0], next[1], map) and next not in targets:
            targets.add(next)
            find_targets_in_range(next, delay - 1, map, targets)
    return targets

def find_shortcuts(path, map, delay):
    shortcuts = {}
    for pos in path:
        targets = find_targets_in_range(pos, delay, map)
        for target in targets:
            if  map[target[1]][target[0]] != '#':
                saved = int(map[target[1]][target[0]]) - int(map[pos[1]][pos[0]]) - 2
                if saved > 0:
                    shortcuts[saved] = shortcuts.get(saved, 0) + 1
    return shortcuts

def find_shortcuts_2(path, map, delay):
    shortcuts = {}
    for pos in path:
        #print(pos)
        targets = find_targets_in_range(pos, delay, map)
        for target in targets:
            if  map[target[1]][target[0]] != '#':
                saved = int(map[target[1]][target[0]]) - int(map[pos[1]][pos[0]]) - 2
                if saved > 0:
                    shortcuts[saved] = shortcuts.get(saved, 0) + 1
    return shortcuts

def part_one():
    map = [list(line.strip()) for line in open(filename)]
    path = bfs(map, get_start(map))
    shortcuts = find_shortcuts(path, map, 2)
    return sum(value for key, value in shortcuts.items() if key >= 100)

def part_two():
    map = [list(line.strip()) for line in open(filename)]
    path = bfs(map, get_start(map))
    shortcuts = find_shortcuts_2(path, map, 20)
    print(shortcuts)
    return sum(value for key, value in shortcuts.items() if key >= 50)

def main():
    print("#1 -> ", part_one())
    print("#2 -> ", part_two())
main()