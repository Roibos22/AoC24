import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt"if test else "input.txt"

def parse_data(filename):
    with open(filename) as file:
        patterns = [pattern.strip() for pattern in file.readline().split(',')]
        file.readline()
        designs = [line.strip() for line in file.readlines()]
    return patterns, designs

cache = {}
def find_design(patterns, design):
    result = 0
    if design == "":
        return 1
    if design in cache:
        return cache[design]
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            result += find_design(patterns, design[len(pattern):])
    cache[design] = result
    return result

def main():
    patterns, designs = parse_data(filename)
    print("#1 -> ", len([design for design in designs if find_design(patterns, design) > 0]))
    print("#2 -> ", sum(find_design(patterns, design) for design in designs))

main()