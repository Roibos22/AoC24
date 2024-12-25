import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def parse_data(filename):
    locks, keys, block = [], [], []
    with open(filename) as file:
        for line in list(file) + ['\n']:
            line = line.strip()
            if line == "":
                heights = []
                for col in zip(*block):
                    count = 0
                    for row in col:
                        if row == '#':
                            count += 1
                    heights.append(count - 1)
                if block[0] == '#####':
                    locks.append(heights)
                if block[-1] == '#####':
                    keys.append(heights)
                block = []
            else:
                block.append(line)
    return locks, keys

def part_one(locks, keys):
    count = 0
    for lock in locks:
        for key in keys:
            fits = True
            for col in zip(lock, key):
                if col[0] + col [1] > 5:
                    fits = False
            if fits:
                count += 1

    return count


def main():
    locks, keys = parse_data(filename)
    
    print("#1 -> ", part_one(locks, keys))
    #print("#2 -> ", part_two())

main()