import sys
from collections import deque

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def print_map(map):
    for row in map:
        wide_chars = [str(char).center(3) if char != "'" else "   " for char in row]
        print(''.join(wide_chars))
    print()

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


seen = set()
def find_targets_in_range(pos, delay, map, targets=None):
   #print(pos, delay)
    if targets is None: targets = set()
    targets.add((pos, 20 - delay))
    if delay <= 0: return targets

    for dx, dy in dirs:
        next = (pos[0] + dx, pos[1] + dy)
        if in_range(next[0], next[1], map) and (next, delay - 1) not in targets:
            find_targets_in_range(next, delay - 1, map, targets)
    return targets

def find_shortcuts(path, map, delay):
    shortcuts = {}
    for pos in path:
        #print(pos)
        targets = find_targets_in_range(pos, delay, map)
        for target in targets:
            if  map[target[0][1]][target[0][0]] != '#':
                saved = int(map[target[0][1]][target[0][0]]) - int(map[pos[1]][pos[0]]) - 2
                if saved > 0:
                    shortcuts[saved] = shortcuts.get(saved, 0) + 1
    return shortcuts

def find_shortcuts_2(path, map, delay):
    shortcuts = {}
    for pos in path:
        #print(pos)
        targets = find_targets_in_range(pos, delay, map)
        #print(targets)
        print("---")
        for target in targets:
            if  map[target[0][1]][target[0][0]] != '#':

                saved = int(map[target[0][1]][target[0][0]]) - int(map[pos[1]][pos[0]]) - (20 - target[1])
                if saved > 0:
                    shortcuts[saved] = shortcuts.get(saved, 0) + 1
    return shortcuts

def part_one():
    map = [list(line.strip()) for line in open(filename)]
    path = bfs(map, get_start(map))
    shortcuts = find_shortcuts(path, map, 2)
    return sum(value for key, value in shortcuts.items() if key >= 100)

def add_path_to_map(map, path):
    for i, pos in enumerate(path):
        map[pos[1]][pos[0]] = i
    return map

def get_targets(path, map, delay):
    targets = [] # (pos, [targets])
    for pos in path:
        pos_targets = set()
        for s in range(1, delay):
            for dx in range(s):
                dy = s - dx
                for x, y in {(pos[0] + dx, pos[1] + dy), (pos[0] - dx, pos[1] + dy), (pos[0] + dx, pos[1] - dy), (pos[0] - dx, pos[1] - dy)}:
                    if in_range(x, y, map) and map[y][x] != '#':
                        pos_targets.add((x, y))
        print((pos, pos_targets))
        targets.append((pos, pos_targets))
    return targets

def get_reachables(map, path_pos, radius):
    reachables = set()
    for dx in range(-radius, radius + 1):
        for dy in range(-radius + abs(dx), radius - abs(dx) + 1):
            nx, ny = path_pos[0] + dx, path_pos[1] + dy
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]):
                if ((nx, ny) != path_pos):
                    if (map[ny][nx] != '#'):
                        reachables.add((nx, ny))
    return reachables

def part_two():
    shortcuts = {}
    map = [list(line.strip()) for line in open(filename)]
    path = bfs(map, get_start(map))
    map = add_path_to_map(map, path)
    for path_pos in path:
        reachables = get_reachables(map, path_pos, 20)
        for target in reachables:
            steps = abs(path_pos[0] - target[0]) + abs(path_pos[1] - target[1])
            time_safed = map[target[1]][target[0]] - map[path_pos[1]][path_pos[0]] - steps
            if (time_safed >= 100):
                shortcuts[time_safed] = shortcuts.get(time_safed, 0) + 1
    return sum(value for key, value in shortcuts.items())

def main():
    print("#1 -> ", part_one())
    print("#2 -> ", part_two())

main()