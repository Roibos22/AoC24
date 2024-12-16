import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == 'test' else False
filename = "input_test.txt" if test else 'input.txt'

def parse_data(filename):
    map = [list(line) for line in open(filename).read().split("\n\n")[0].splitlines()]
    moves = open(filename).read().split("\n\n")[1].replace('\n', '')
    return map, moves

def print_map(map):
    for line in map:
        print(''.join(line))

def get_start_pos(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '@':
                return (x, y)

dirs = {
    ">": (1, 0),
    "<": (-1, 0),
    "^": (0, -1),
    "v": (0, 1)
}

def is_move_possible(map, pos, move):
    dx, dy = dirs[move]
    tmp_pos = (pos[0] + dx, pos[1] + dy)
    while(map[tmp_pos[1]][tmp_pos[0]] in 'O[]'):
        tmp_pos = (tmp_pos[0] + dx, tmp_pos[1] + dy)
    if (map[tmp_pos[1]][tmp_pos[0]] == '#'):
            return False
    return True

def make_move(map, pos, move):
    dx, dy = dirs[move]
    boxes_in_front = 0
    tmp_pos = (pos[0] + dx, pos[1] + dy)
    while (map[tmp_pos[1]][tmp_pos[0]] == 'O'):
        boxes_in_front += 1
        tmp_pos = (tmp_pos[0] + dx, tmp_pos[1] + dy)

    map[pos[1]][pos[0]] = '.'
    pos = (pos[0] + dx, pos[1] + dy)
    map[pos[1]][pos[0]] = '@'

    tmp_pos = pos
    while(boxes_in_front > 0):
        tmp_pos = (tmp_pos[0] + dx, tmp_pos[1] + dy)
        map[tmp_pos[1]][tmp_pos[0]] = 'O'
        boxes_in_front -= 1

    return pos

def gps_sum(map, char):
    res = 0
    for y, row in enumerate(map):
        for x, c in enumerate(row):
            if c == char:
                res += 100 * y + x
    return res

def part_one(map, moves):
    pos = get_start_pos(map)
    for move in moves:
        if is_move_possible(map, pos, move):
            pos = make_move(map, pos, move)
    return(gps_sum(map, 'O'))

def convert_map(map):
    new_map = []
    for y, row in enumerate(map):
        new_row = []
        for x, char in enumerate(row):
            if char == '#':
                new_row.extend(['#', '#'])
            elif char == 'O':
                new_row.extend(['[', ']'])
            elif char == '.':
                new_row.extend(['.', '.'])
            elif char == '@':
                new_row.extend(['@', '.'])

        new_map.append(new_row)
    return new_map

def make_move_2(map, pos, move):
    dx, dy = dirs[move]
    boxes = [pos]

    for box in boxes:
        next_pos = (box[0] + dx, box[1] + dy)
        if next_pos in boxes:
            continue
        if map[next_pos[1]][next_pos[0]] == "[":
            boxes.append(next_pos)
            boxes.append((next_pos[0] + 1, next_pos[1]))
        if map[next_pos[1]][next_pos[0]] == "]":
            boxes.append(next_pos)
            boxes.append((next_pos[0] - 1, next_pos[1]))
        if map[next_pos[1]][next_pos[0]] == "#":
            return pos

    new_positions = []
    for box in boxes:
        new_positions.append(((box[0] + dx, box[1] + dy),  map[box[1]][box[0]]))
        map[box[1]][box[0]] = '.'
    for box in new_positions:
        map[box[0][1]][box[0][0]] = box[1]

    return get_start_pos(map)

def part_two(map, moves):
    map = convert_map(map)
    pos = get_start_pos(map)
    for move in moves:
        pos = make_move_2(map, pos, move)
    return(gps_sum(map, '['))


def main():
    map, moves = parse_data(filename)
    print("#1 -> ", part_one(map, moves))
    map, moves = parse_data(filename)
    print("#2 -> ", part_two(map, moves))

main()
