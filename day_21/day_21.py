import sys
from collections import deque

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

num_kb = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [None, '0', 'A']
]

dir_kb = [
    [None, '^', 'A'],
    ['<', 'v', '>']
]

dirs = [((0, 1), 'v'), ((1, 0), '>'), ((0, -1), '^'), ((-1, 0), '<')]

dir_1_pos = (2, 0)
dir_2_pos = (2, 0)
num_pos = (2, 3)


def find_all_sequences_from_to(kb, pos1, pos2):
    print(pos1, "to", pos2)

    if pos1 == pos2:
        return ((pos1, pos2), "A")

    shortest_paths = []
    q = deque([(, "")])
    shortest = float("inf")

    while q:
        print(q.popleft())
        (y, x), moves = q.popleft()
        print((y, x), moves)



# find all shortest sequence to get from any button to every other button
def find_all_sequences(keyboard):
    sequences = {} # (from, to): [seq1, seq2, ...]

    # create keyboard positions
    positions = {} # value : (y, x)
    for y in range(len(keyboard)):
        for x in range(len(keyboard[y])):
            if keyboard[y][x]:
                positions[keyboard[y][x]] = (y, x)
    print(positions)

    for pos1 in positions:
        for pos2 in positions:
            print(find_all_sequences_from_to(pos1, pos2))

    return None

def part_one(codes):
    print(codes)
    sequences = find_all_sequences(num_kb)
    print(sequences)
    return None

def main():
    data = [list(line.strip()) for line in open(filename)]
    print('#1 -> ', part_one(data))

main()