import sys
from typing import List, Dict, Tuple

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def is_in_range(x, y, map):
    return (
        x >= 0 and
        y >= 0 and\
        y < len(map) and\
        x < len(map[y])
    )

def is_neighbour(pos0, pos1, map):
    # if map[pos0[1]][pos0[0]] == "I":
        # print("checking neighbours", pos0, pos1)
    if is_in_range(pos1[0], pos1[1] - 1, map) and pos0[0] == pos1[0] and pos0[1] == pos1[1] - 1:
        # print("neighbour at", pos0, pos1)
        return True
    elif is_in_range(pos1[0], pos1[1] + 1, map) and pos0[0] == pos1[0] and pos0[1] == pos1[1] + 1:
        # print("neighbour at", pos0, pos1)
        return True
    elif is_in_range(pos1[0] - 1, pos1[1], map) and pos0[0] == pos1[0] - 1 and pos0[1] == pos1[1]:
        # print("neighbour at", pos0, pos1)
        return True
    elif is_in_range(pos1[0] + 1, pos1[1], map) and pos0[0] == pos1[0] + 1 and pos0[1] == pos1[1]:
        # print("neighbour at", pos0, pos1)
        return True
    return False

def add_to_touching_area(areas, x, y, map):
    for i in range(len(areas)):
        for j in range(len(areas[i])):
            # print(areas[i][j])
            if is_neighbour([areas[i][j][0], areas[i][j][1]], [x, y], map):
                # print("Neighbour found")
                areas[i].append([x, y])
                return True
    # print("No Neighbour found")
    return False

def add_to_areas(x, y, areas, char, map):
    if char in areas:
        # print("existing char in dict found", char)
        if not add_to_touching_area(areas[char], x, y, map):
            areas[char].append([[x, y]])
        
    if char not in areas:
        # print("no char in dict found")
        areas[char] = []
        areas[char].append([[x, y]])
    # print(areas)
    return

def find_fences_for_pos(pos0, area, map):
    neighbours = 0
    # print("check", pos0, area)
    for pos1 in area:
        if is_neighbour(pos0, pos1, map):
            neighbours += 1
    # print(neighbours)
    # print(4 - neighbours, "fences for pos", pos0)
    return 4 - neighbours

def calc_price(areas, map):
    price = 0
    # print("CALCULATING...")
    for i in areas:
        # print("-----")
        # print(map[areas[i][0][0][1]][areas[i][0][0][0]])
        for j in range(len(areas[i])):
            fences = 0
            for pos in areas[i][j]:
                fences += find_fences_for_pos(pos, areas[i][j], map)
            # print(areas[i][j])
            # print(fences, len(areas[i][j]))
            price += fences * len(areas[i][j])
    return price

def merge_areas(areas, map):
    keys = list(areas.keys())
    merged = True

    while merged:
        merged = False
        for key in keys:
            i = 0
            while i < len(areas[key]):
                area1 = areas[key][i]
                j = i + 1
                # Compare each pos in area with each pos in all later areas
                while j < len(areas[key]):
                    area2 = areas[key][j]
                    merge_found = False
                    for pos1 in area1:
                        for pos2 in area2:
                            if is_neighbour(pos1, pos2, map):
                                # Merge areas
                                area1.extend(area2)
                                # Remove area2
                                areas[key].pop(j)
                                merged = True
                                merge_found = True
                                break
                        if merge_found:
                            break
                    if merge_found:
                        continue
                    j += 1
                i += 1
                
    return areas


def part_one(map):
    areas: Dict[str, List[List[Tuple[int, int]]]] = {}
    for y in range(len(map)):
        for x in range(len(map[y])):
            # print("adding", map[y][x], x, y)
            add_to_areas(x, y, areas, map[y][x], map)
    
    merge_areas(areas, map)
    return calc_price(areas, map)

def main():
    data = [list(line.strip()) for line in open(filename)]
    print(data)
    print("#1 -> ", part_one(data))

main()