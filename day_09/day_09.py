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

spaces_index = 0

def get_upcoming_spaces(line, i):
    global spaces_index
    spaces_index = i  # Start counting from current position
    count = 0
    while((spaces_index + count < len(line)) and line[spaces_index + count] == '.'):
        count += 1
    print(f"Found {count} spaces at index {spaces_index}")
    return count

def insert_block_at_index(line, block, i):
    while block[1] > 0:
        line[i] = block[0]
        line[block[3]] = '.'
        block[1] -= 1
        block[3] += 1
        i += 1
    return line

def part_two(data):
    global spaces_index
    spaces_index = 0  # Initialize once at start
    line = create_line(data)
    print(line)
    # iterate over data from end
    for block in reversed(data):
        print(block)
        upcoming_spaces = get_upcoming_spaces(line, spaces_index)
        while (upcoming_spaces < block[1] or spaces_index > block[3]) and spaces_index < len(line):  # Add length check
            spaces_index += 1
            upcoming_spaces = get_upcoming_spaces(line, spaces_index)
            
        if upcoming_spaces >= block[1] and spaces_index <= block[3]:
            line = insert_block_at_index(line, block, spaces_index)
    print(line)
    return get_checksum(line)
    # get checksum

def main():
    global spaces_index
    data = parse_data()
    # print(data)
    
    part_one(data)
    print("#1 -> ", part_one(data))
    spaces_index = 0
    print("#2 -> ", part_two(data))

main()