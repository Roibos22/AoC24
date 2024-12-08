import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"
antinodes_part_1 = set()
antinodes_part_2 = set()
map = [list(line.strip()) for line in open(filename)]

def get_antennas_dict():
    global map
    antennas_dict = {}
    for y in range(len(map)):
        for x in range(len(map[y])):
            if (map[y][x].isalpha() or map[y][x].isalnum()):
                if map[y][x] not in antennas_dict:
                    antennas_dict[map[y][x]] = []
                antennas_dict[map[y][x]].append((x, y))
    return antennas_dict

def is_in_map(antinode):
    global map
    return (
        antinode[0] >= 0 and\
        antinode[1] >= 0 and\
        antinode[0] < len(map[0]) and\
        antinode[1] < len(map)
    )

def create_antinodes_part_1(coord1, coord2):
    global map
    delta = (coord2[0] - coord1[0], coord2[1] - coord1[1])

    antinode1 = (coord1[0] - delta[0], coord1[1] - delta[1])
    antinode2 = (coord2[0] + delta[0], coord2[1] + delta[1])

    if is_in_map(antinode1): antinodes_part_1.add(antinode1)
    if is_in_map(antinode2): antinodes_part_1.add(antinode2)

def create_antinodes_part_2(coord1, coord2):
    global map
    delta = (coord2[0] - coord1[0], coord2[1] - coord1[1])
    antinodes_part_2.add(coord1)
    antinodes_part_2.add(coord2)

    while True:
        coord1 = (coord1[0] - delta[0], coord1[1] - delta[1])
        if is_in_map(coord1):
            antinodes_part_2.add(coord1)
        else:
            break
    
    while True:
        coord2 = (coord2[0] + delta[0], coord2[1] + delta[1])
        if is_in_map(coord2):
            antinodes_part_2.add(coord2)
        else:
            break

def main():
    global map
    antennas_dict = get_antennas_dict()

    for antenna, coords in antennas_dict.items():
        for i, coord in enumerate(coords):
            for j in range(i + 1, len(coords)):
                create_antinodes_part_1(coords[i], coords[j])
                create_antinodes_part_2(coords[i], coords[j])
    
    print("#1 ->", len(antinodes_part_1))
    print("#2 ->", len(antinodes_part_2))

main()