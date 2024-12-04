data = []

with open('input.txt', 'r') as file:
    data = [line.strip() for line in file]

def in_range(y, x):
    return (y >= 0 and y < len(data) and 
            x >= 0 and x < len(data[y]))

# PART 1

directions_part_1 = [
    (-1, -1), (+0, -1), (+1, -1),
    (-1, +0),           (+1, +0),
    (-1, +1), (+0, +1), (+1, +1)
]

def check_xmas(y, x, count):
    str = "XMAS"

    for dx, dy in directions_part_1:
        tmp_x, tmp_y = x, y
        for i in range(len(str)):
            if not in_range(tmp_y, tmp_x) or str[i] != data[tmp_y][tmp_x]:
                break
            tmp_y += dy; tmp_x += dx
            if i == len(str) - 1:
                count += 1
    return count

# PART 2

directions_part_2 = [
    (-1, -1), (+1, -1),
    (-1, +1), (+1, +1)
]

def check_x_mas(y, x, count):
    if not data[y][x] == 'A': return count

    matches = 0
    for dx, dy in directions_part_2:
        if (in_range(y + dy, x + dx) and data[y + dy][x + dx] == 'M') and \
           (in_range(y - dy, x - dx) and data[y - dy][x - dx] == 'S'):
            matches += 1

    if matches == 2: 
        return count + 1

    return count

def main():
    count_part_1 = 0
    count_part_2 = 0
    for y in range(len(data)):
        for x in range(len(data[y])):
            count_part_1 = check_xmas(y, x, count_part_1)
            count_part_2 = check_x_mas(y, x, count_part_2)
    print("#1 ->", count_part_1)
    print("#2 ->", count_part_2)

main()