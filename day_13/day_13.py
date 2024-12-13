import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == 'test' else False
filename = "input_test.txt" if test else "input.txt"

((), (), ())

def parse_data(filename):
    data = []
    lines = []
    with open(filename, 'r') as file:
        lines = [line.strip() for line in file if line.strip()]
        for i in range(0, len(lines), 3):
            if i+2 >= len(lines): break
            a_x = int(lines[i].split('+')[1].split(',')[0])
            a_y = int(lines[i].split('+')[2])
            b_x = int(lines[i+1].split('+')[1].split(',')[0])
            b_y = int(lines[i+1].split('+')[2])
            p_x = int(lines[i+2].split('=')[1].split(',')[0])
            p_y = int(lines[i+2].split('=')[2])
            data.append([(a_x, a_y), (b_x, b_y), (p_x, p_y)])
    return (data)

def is_multiple(x, y, dx, dy, mx, my):
    diff_x = mx - x
    diff_y = my - y
    if (diff_x / dx) % 1 == 0 and (diff_y / dy) % 1 == 0:
        return (int(diff_x / dx))
    return False

def part_one(machienes):
    tokens = 0
    for machiene in machienes:
        print(machiene)
        A = 0
        B = 0
        x = 0
        y = 0
        if is_multiple(x, y, machiene[1][0], machiene[1][1], machiene[2][0], machiene[2][1]):
            tokens += is_multiple(x, y, machiene[1][0], machiene[1][1], machiene[2][0], machiene[2][1])
            print("B multiple")
        else:
            while not is_multiple(x, y, machiene[0][0], machiene[0][1], machiene[2][0], machiene[2][1]) and B <= 100:
                x += machiene[1][0]
                y += machiene[1][1]
                B += 1
            A = is_multiple(x, y, machiene[0][0], machiene[0][1], machiene[2][0], machiene[2][1])
            if A:
                tokens += (A * 3) + B
    return tokens

def main():
    machienes = parse_data(filename)
    print("#1 -> ", part_one(machienes))

main()