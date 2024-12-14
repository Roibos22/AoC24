import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == 'test' else False
filename = "input_test.txt" if test else "input.txt"

# using regex would have been way cooler and easier...
def parse_data(filename):
    data = []
    with open(filename) as file:
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

# machine = [(ax, ay), (bx, by), (Px, Py)]
# A = ((Px * by) - (Py * bx)) / ((ax * by) - (ay * bx))
# B = (Px - (A * ax)) / bx

def calc_tokens(machines):
    tokens = 0
    for machine in machines:
        (ax, ay), (bx, by), (Px, Py) = machine
        A = ((Px * by) - (Py * bx)) / ((ax * by) - (ay * bx))
        B = (Px - (A * ax)) / bx
        if A % 1 == 0 and B % 1 == 0:
            tokens += int(B + A * 3)
    return(tokens)

def part_two(machines):
    for machine in machines:
        machine[2] = (machine[2][0] + 10000000000000, machine[2][1] + 10000000000000)
    return calc_tokens(machines)

def main():
    machines = parse_data(filename)
    print("#1 -> ", calc_tokens(machines))
    print("#2 -> ", part_two(machines))

main()