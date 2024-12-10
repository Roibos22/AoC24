import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

directions = (
        (-1,  0),
    ( 0, -1), ( 0,  1),
        ( 1,  0)
)

def is_in_range(y, x, data):
    return (
        x >= 0 and\
        y >= 0 and\
        x < len(data[0]) and\
        y < len(data)
    )

# PART 1

def part_one(data):
    trailheads = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                trailheads_set = set()
                trailheads += find_path_part_one(x, y, data, trailheads_set)
    return trailheads

def find_path_part_one(x, y, data, trailheads):
    for dir in directions:
        new_x, new_y = x + dir[0], y + dir[1]
        if is_in_range(new_y, new_x, data):
            if data[new_y][new_x] == data[y][x] + 1:
                if data[new_y][new_x] == 9:
                    trailheads.add((new_x, new_y))
                else:
                    find_path_part_one(new_x, new_y, data, trailheads)
    return len(trailheads)

# PART 2

def part_two(data):
    trailheads = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == 0:
                trailheads += find_path_part_two(x, y, data)
    return trailheads

def find_path_part_two(x, y, data):
    trailheads = 0
    for dir in directions:
        new_x, new_y = x + dir[0], y + dir[1]
        if is_in_range(new_y, new_x, data):
            if data[new_y][new_x] == data[y][x] + 1:
                if data[new_y][new_x] == 9:
                    trailheads += 1
                else:
                    trailheads += find_path_part_two(new_x, new_y, data)
    return trailheads

def main():
    data = [list(map(int, line.strip())) for line in open(filename)]
    print("#1 -> ", part_one(data))
    print("#2 -> ", part_two(data))
main()