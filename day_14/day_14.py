import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == 'test' else False
filename = "input_test.txt" if test else "input.txt"

def parse_data(filename):
    data = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        for line in lines:
            x = int(line.split('=')[1].split(',')[0])
            y = int(line.split(',')[1].split()[0])
            vx = int(line.split('=')[2].split(',')[0])
            vy = int(line.split(',')[2].split()[0])
            data.append([[x, y], (vx, vy)])
    return (data)

def get_map(robots, width, length):
    map = [[0 for x in range(width)] for y in range(length)]
    for robot in robots:
        map[robot[0][1]][robot[0][0]] += 1
    return map

def print_map(map):
    for row in map:
        for value in row:
            if value == 0:
                print(' ', end='')
            else:
                print(value, end='')
        print()

def simulate(robots, width, length, seconds):
    for i in range(seconds):
        for robot in robots:
            robot[0][0] = (robot[0][0] + robot[1][0]) % width
            robot[0][1] = (robot[0][1] + robot[1][1]) % length
        # for part two, fucks performance...
        get_safety_factor(get_map(robots, width, length), width, length, i)
    return robots

def get_safety_factor(map, width, lenght, i):
    q1 = q2 = q3 = q4 = 0
    half_x = (width-1)//2
    half_y = (lenght-1)//2
    for x in range(lenght):
        for y in range(width):
            if x == half_y or y == half_x:
                continue
            if x < half_y and y < half_x:
                q1 += map[x][y]
            elif x < half_y and y > half_x:
                q2 += map[x][y]
            elif x > half_y and y < half_x:
                q3 += map[x][y]
            elif x > half_y and y > half_x:
                q4 += map[x][y]
    sf = q1 * q2 * q3 * q4
    safety_factors.append([sf, i])
    return(sf)

safety_factors = []

def part_one(width, length):
    robots = parse_data(filename)
    robots = simulate(robots, width, length, 100)
    map = get_map(robots, width, length)
    return(get_safety_factor(map, width, length, 0))

def part_two(width, length):
    global safety_factors
    safety_factors = []
    robots = parse_data(filename)
    robots = simulate(robots, width, length, 10000)
    map = get_map(robots, width, length)
    return(min(safety_factors, key=lambda x: x[0])[1] + 1)

def main():
    width, length = 101, 103
    print("#1 -> ", part_one(width, length,))
    print("#2 -> ", part_two(width, length,))

main()