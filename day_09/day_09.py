import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

# [ [id, len, spaces, start_index] ]
def parse_data():
    data = []
    start_index = 0
    with open(filename, 'r') as file:
        for line in file:
            for i in range(0, len(line), 2):
                spaces = int(line[i+1] if i+1 < len(line) else 0)
                data.append([int(i/2), int(line[i]), spaces, start_index])
                start_index = start_index + spaces + int(line[i])
    return data

def create_line(data):
    line = []
    for block in data:
        line.extend([block[0]] * block[1])
        line.extend(['.'] * block[2])
    return line

def get_checksum(line):
    sum = 0
    for i, num in enumerate(line):
        if num != '.':
            sum += i * num
    return sum

def remove_dots_at_back(line):
    for i, char in enumerate(reversed(line)):
        if char == '.':
            line.pop(-1)
        else:
            return line
    return line

def get_next_char_from_back(line):
    for i, char in enumerate(reversed(line)):
        if char != '.':
            line[len(line) - i - 1] = '.'
            return char
    return '.'

def part_one(data):
    line = create_line(data)
    for i, char in enumerate(line):
        if char == '.':
            line[i] = get_next_char_from_back(line)
            line = remove_dots_at_back(line)
    return get_checksum(line)

def get_upcoming_spaces(line, needed_spaces):
    for i in range(len(line)):
        if line[i] == '.':
            count = 0
            while((i + count < len(line)) and line[i + count] == '.'):
                count += 1
            if count >= needed_spaces:
                return count, i
    return 0, 0

def insert_block_at_index(line, block, i):
    while block[1] > 0:
        line[i] = block[0]
        line[block[3]] = '.'
        block[1] -= 1
        block[3] += 1
        i += 1
    return line

def part_two(data):
    line = create_line(data)
    for block in reversed(data):
        spaces, space_index = get_upcoming_spaces(line, block[1])
        if spaces >= block[1] and space_index <= block[3]:
            line = insert_block_at_index(line, block, space_index)
    return get_checksum(line)

def main():
    data = parse_data()
    print("#1 -> ", part_one(data))
    print("#2 -> ", part_two(data))

main()