import sys
from typing import List, Dict, Tuple

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"
map = [list(line.strip()) for line in open(filename)]

dirs = (
        (0 , -1),
    (-1,  0), (+1,  0),
        ( 0, +1)
)

# corner_dirs = (
#     (-0.5 , -0.5), (+0.5, -0.5),
#     (-0.5 , +0.5), (+0.5, +0.5)
# )

corner_dirs = (
    (-0.5, -0.5),  # top-left
    (-0.5, +0.5),  # bottom-left
    (+0.5, +0.5),  # bottom-right
    (+0.5, -0.5)   # top-right
)

def in_range(x, y):
    return (
        x >= 0 and
        y >= 0 and\
        y < len(map) and\
        x < len(map[y])
    )

def flood_fill(pos, current_area):
    if pos in seen: 
        return

    seen.add(pos)
    if current_area is None:
        current_area = []
        areas.append(current_area)
    current_area.append(pos)

    for dir in dirs:
        new_pos = (pos[0] + dir[0], pos[1] + dir[1])
        if (in_range(new_pos[0], new_pos[1]) and 
            new_pos not in seen and
            map[new_pos[1]][new_pos[0]] == map[pos[1]][pos[0]]):
            flood_fill(new_pos, current_area)

def calc_price(areas, map):
    price = 0
    for area in areas:
        fences = 0
        for pos in area:
            for dir in dirs:
                new_pos = (pos[0] + dir[0], pos[1] + dir[1])
                if not in_range(new_pos[0], new_pos[1]) or new_pos not in area:
                   fences += 1
        price += fences * len(area)
    return price

seen = set()
areas = []

def part_one(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            flood_fill((x, y), None)
    return (calc_price(areas, map))

def part_two(map):
    price = 0
    print(areas)
    for area in areas:
        corners = 0
        area_char = map[area[0][1]][area[0][0]]
        # print(area_char)
        area_corners = set()
        # print(area)
        for pos in area:
            for dir in corner_dirs:
                area_corners.add((pos[0] + dir[0], pos[1] + dir[1]))
        # print("area corners", area_corners)
        for corner in area_corners:
            # for each touching field of a corner in a region create config of 'if are same area'
            # print(corner)
            config = []
            for dir in corner_dirs:
                pos = [int(corner[0] + dir[0]), int(corner[1] + dir[1])]
                # print(pos)
                config.append(True) if in_range(pos[0], pos[1]) and area_char == map[pos[1]][pos[0]] else config.append(False)
            count = sum(config)
            # print("corner", corner, "has conf ", config)
            if count == 1:
                corners += 1
            elif count == 2:
                if config == [True, False, True, False] or config == [False, True, False, True]:
                    corners += 2
            elif count == 3:
                corners += 1
        # print(corners)
        print("area ", area_char, corners, len(area))
        price += corners * len(area)
    return price
    # count corners
    # for every pos check to 


def main():
    print("#1 -> ", part_one(map))
    print("#2 -> ", part_two(map))


main()