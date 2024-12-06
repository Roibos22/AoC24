original_map = [list(line.strip()) for line in open('input.txt')]
directions = [
        ['^', ( 0, -1), '|'],
        ['>', ( 1,  0), '-'],
        ['v', ( 0, +1), '|'],
        ['<', (-1,  0), '-'],
    ]
pos = [0, 0]

def print_map(map):
    for i, line in enumerate(map):
        print(f"{i:2} ", end='')  # Row number with 2 spaces for alignment
        print(''.join(line), end='\n\n')
    

def find_pos(map):
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            for d in directions:
                if d[0] == char:
                    return d, [x, y]
    return None, None

def in_range(map, x, y):
    return (
        x >= 0 and\
        y >= 0 and\
        x <  len(map[0]) and\
        y < len(map)
    )

walked_positions_part_1 = set()

def part_one():
    global directions, walked_positions_part_1
    map = [row[:] for row in original_map]
    dir, pos = find_pos(map)
    while(in_range(map, pos[0], pos[1])):
        next_y = pos[1] + dir[1][1]
        next_x = pos[0] + dir[1][0]
            
        if in_range(map, next_x, next_y):
            if map[next_y][next_x] == '#':
                cur_i = directions.index(dir)
                next_i = (cur_i + 1) % len(directions)
                dir = directions[next_i]

        if not map[pos[1]][pos[0]] == 'x':
            map[pos[1]][pos[0]] = 'x'
            walked_positions_part_1.add((pos[0], pos[1]))
        pos[1] += dir[1][1]
        pos[0] += dir[1][0]

    return len(walked_positions_part_1)

def is_visited(visited, pos, dir_char):
    pos_with_dir = (pos[0], pos[1], dir_char)
    return pos_with_dir in visited

def is_infinite_loop(map, init_pos, dir):
    pos = (init_pos[0], init_pos[1], dir[0])
    visited = set()

    while(in_range(map, pos[0], pos[1])):

        if pos in visited:
            return 1
        visited.add(pos)

        # mark position
        if map[pos[1]][pos[0]] in '-|+':
            map[pos[1]][pos[0]] = '+'
        elif map[pos[1]][pos[0]] == '.':
            map[pos[1]][pos[0]] = dir[2]

        # change direction if obstacle
        if in_range(map, pos[0] + dir[1][0], pos[1] + dir[1][1]):
            while map[pos[1] + dir[1][1]][pos[0] + dir[1][0]] == '#':
                map[pos[1]][pos[0]] = '+'
                dir = directions[(directions.index(dir) + 1) % len(directions)]

        pos = (pos[0] + dir[1][0], pos[1] + dir[1][1], dir[0])
    return 0

def part_two():
    count = 0
    map = [row[:] for row in original_map]
    initial_dir, initial_pos = find_pos(map)
    
    for y in range(len(map)):
        for x in range(len(map[y])):
          if (x, y) in walked_positions_part_1:
                tmp_pos = initial_pos[:]
                tmp_dir = initial_dir[:]
                tmp_map = [row[:] for row in map]
                tmp_map[y][x] = '#'
                tmp_map[tmp_pos[1]][tmp_pos[0]] = '.'
                count += is_infinite_loop(tmp_map, tmp_pos, tmp_dir)
    return count

def main():
    print("#1 -> ", part_one())
    print("#2 -> ", part_two())

main()