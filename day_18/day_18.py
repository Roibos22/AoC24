import sys
from collections import deque

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt"if test else "input.txt"
length = 7 if test else 71
fallen_bytes = 12 if test else 1024

dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def print_grid(grid, path = None):
    if path:
        for (x, y) in path:
            grid[y][x] = 'O'
    for y in grid:
        print(''.join(y))

def populate_grid(grid, coords):
    for i in range(fallen_bytes):
        coord = coords[i]
        grid[coord[1]][coord[0]] = '#'

def valid_pos(pos):
    return (
        pos[0] >= 0 and\
        pos[1] >= 0 and\
        pos[0] < length and\
        pos[1] < length
    )

def bfs(grid):
    q = deque([ ((0, 0), [(0, 0)]) ]) # [ pos, [path] ]
    visited = {(0, 0)}

    while q:
        pos, path = q.popleft()
        if (pos == (length - 1, length - 1)):
            return (path)

        for dx, dy in dirs:
            next_pos = (pos[0] + dx, pos[1] + dy)

            if valid_pos(next_pos) and grid[next_pos[1]][next_pos[0]] != '#' and next_pos not in visited:
                visited.add(next_pos)
                q.append((next_pos, path + [next_pos]))

    return None

def part_one(grid, coords):
    populate_grid(grid, coords)
    path = bfs(grid)
    return(len(path) - 1)

def part_two(grid, coords):
    for i, coord in enumerate(coords):
        grid[coord[1]][coord[0]] = '#'
        if not bfs(grid):
            return coords[i]

def main():
    grid = [['.'] * length for _ in range(length)]
    coords = [tuple(map(int, line.strip().split(','))) for line in open(filename)]
    print("#1 -> ", part_one(grid, coords))
    print("#2 -> ", part_two(grid, coords))

main()