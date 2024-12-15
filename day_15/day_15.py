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

def gps_sum(map):
    res = 0
    for y, row in enumerate(map):
        for x, char in enumerate(row):
            if char == 'O':
                res += 100 * y + x
    return res

def part_one(map, moves):
    pos = get_start_pos(map)
    for move in moves:
        if is_move_possible(map, pos, move):
            pos = make_move(map, pos, move)
    return(gps_sum(map))

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
    next_x, next_y = pos
    boxes = []

    while(42):
        possible = True
        check_more = False
        current_boxes = [(next_x, next_y)]
        boxes.extend(current_boxes)
        print("boxes", boxes)
        
        new_boxes = []
        for box in boxes:
            next_x = box[0] + dx
            next_y = box[1] + dy
            if map[next_y][next_x] == '[':
                new_boxes.extend([(next_x, next_y), (next_x + 1, next_y)])
                check_more = True
            elif map[next_y][next_x] == ']':
                new_boxes.extend([(next_x, next_y), (next_x - 1, next_y)])
                check_more = True
            elif map[next_y][next_x] == '#':
                possible = False
                return pos
        
        if not check_more:
            break
            
        boxes.extend(new_boxes)
        boxes = list(set(boxes))
        print("1")
    
    print("real:", boxes)
        # print(boxes)
    print("SET")
    boxes = list(set(boxes))
    print(boxes)
    # for box in boxes:
    #     print(box)

    return pos

def part_two(map, moves):
    map = convert_map(map)
    print_map(map)
    pos = get_start_pos(map)
    print(pos)
    for move in moves:
        if is_move_possible(map, pos, move):
            pos = make_move_2(map, pos, move)
   # return(gps_sum(map))


def main():
    map, moves = parse_data(filename)
    #print("#1 -> ", part_one(map, moves))
    map, moves = parse_data(filename)
    print("#2 -> ", part_two(map, moves))
main()
