import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == 'test' else False
filename = 'input_test.txt' if test else 'input.txt'

# def print_map(map):
#     for line in map:
#         print(line)

# def print_wide_map(maze_map):
#     for row in maze_map:
#         wide_chars = [str(char).center(7) if char != "'" else "   " for char in row]
#         print(''.join(wide_chars))

dirs = {
    1: (0, 1),
    2: (1, 0),
    3: (0, -1),
    4: (-1, 0)
}

def find_pos(map):
    start = ()
    end = ()
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            if char == 'S':
                start = (x, y)
            if char == 'E':
                end = (x, y)
    return start, end

def flood_fill(map, options, end, num):
    while(options):
        new_options = []
        for option in options:
            cost_to_move = int(map[option[0][1]][option[0][0]])
            for key in dirs:
                dir = dirs[key]
                new_cost = 1
                new_pos = (option[0][0] + dir[0], option[0][1] + dir[1])
                if map[new_pos[1]][new_pos[0]] == 'E' :
                    break 
                if map[new_pos[1]][new_pos[0]] != '#':
                    if option[1] != key:
                        new_cost += 1000
                    coming_cost = 0 if map[new_pos[1]][new_pos[0]] == '.' else int(map[new_pos[1]][new_pos[0]])
                    if coming_cost == 0 or cost_to_move + new_cost <= coming_cost:
                        if any(opt[0] == (new_pos[0], new_pos[1]) for opt in new_options):
                            new_options.remove(next(opt for opt in new_options if opt[0] == (new_pos[0], new_pos[1])))
                        map[new_pos[1]][new_pos[0]] = cost_to_move + new_cost
                        new_options.append((new_pos, key))
        options = new_options
    return map

def part_one(map, start, end):
    map[start[1]][start[0]] = 0
    map = flood_fill(map, [(start, 2)], end, 1)
    last_cost = min(map[end[1] + 1][end[0]], map[end[1]][end[0] - 1]) + 1
    map[end[1]][end[0]] = last_cost
    map[start[1]][start[0]] = 0
    return last_cost

def reverse_flood_fill(map, pos):
    cost_current = 0 if map[pos[1]][pos[0]] in ['#', '.', 'O'] else int(map[pos[1]][pos[0]])
    map[pos[1]][pos[0]] = 'O'

    for key in dirs:
        dir = dirs[key]
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])

        diff = cost_current - (0 if map[new_pos[1]][new_pos[0]] in ['#', '.', 'O'] else int(map[new_pos[1]][new_pos[0]]))
        if map[new_pos[1]][new_pos[0]] != "#":
            if diff == 1 or diff == 1001 or (diff == -999 and map[pos[1] - dir[1]][pos[0] - dir[0]] != '#'):
                reverse_flood_fill(map, new_pos)
    
    return map

def part_two(map, end):
    map = reverse_flood_fill(map, end)
    map[end[1] - 1][end[0]] = 'O'
    count = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == 'O':
                count += 1
    return count

def main():
    map = [list(line.strip()) for line in open(filename)]
    start, end = find_pos(map)
    print("#1 -> ", part_one(map, start, end))
    print("#2 -> ", part_two(map, (end[0], end[1] + 1)))

main()