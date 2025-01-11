import sys
from collections import deque

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

# One directional keypad that you are using. 
    # - Output what i press here
# Two directional keypads that robots are using.
    # - two layers
# One numeric keypad (on a door) that a robot is using.
    # final layer

# find shortest path for each button to each other button on numberic keyboard
# translate_to_directional(shortest_path) * 2
    # get shortest paths of each button to each button 

# path to next button is abs(x-x) + abs(y+y) on visual and on directional

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

def in_range(pos, kb):
    return (
        pos[0] >= 0 and\
        pos[1] >= 0 and\
        pos[0] < len(kb[0]) and\
        pos[1] < len(kb)
    )

dir_1_pos = (2, 0)
dir_2_pos = (2, 0)
num_pos = (2, 3)

def find_coord(kb, c):
    for row in range(len(kb)):
        for col in range(len(kb[row])):
            if kb[row][col] == c:
                return (col, row)
    return (0, 0)

def get_valid_moves(pos, kb):
    moves = [] # (new_pos, move)
    for dir, move in dirs:
        next = (pos[0] + dir[0], pos[1] + dir[1])
        if in_range(next, kb) and kb[next[1]][next[0]] != -1:
            moves.append((next, move))
    return moves

def get_all_shortest_paths(fr, to, kb):
    # If already at target, return just 'A'
    if fr == to:
        return [([], ['A'])]

    paths = []  # [(positions), moves]
    dq = deque([(fr, [fr], [])])

    while dq:
        pos, path_to_pos, moves = dq.popleft()

        if pos == to:
            if not paths or len(path_to_pos) < len(paths[0][0]):
                paths = [(path_to_pos, moves)]
            elif len(path_to_pos) == len(paths[0][0]):
                paths.append((path_to_pos, moves))
            continue
        if paths and len(path_to_pos) > len(paths[0][0]):
            continue

        for next_pos, move in get_valid_moves(pos, kb):
            if next_pos not in path_to_pos:
                dq.append((next_pos, 
                          path_to_pos + [next_pos],
                          moves + [move]))
    
    paths = [(path[0][1:], path[1]) for path in paths]
    for path in paths:
        if path and path[0]:  # Only append 'A' if there were moves
            path[1].append('A')
    return paths

def flatten_list(l):
    flat = []
    for row in l:
        flat += row
    return flat

def find_sequence(c):
    global num_pos, dir_1_pos, dir_2_pos
    og_dir_1_pos = dir_1_pos
    og_dir_2_pos = dir_2_pos
    print("-----------------------------")
    print("Finding Sequence to enter ", c)
    print("Possible Paths for Robot 1")
    coord_1 = find_coord(num_kb, c)
    final_final_paths = []
    possible_paths_1 = get_all_shortest_paths(num_pos, coord_1, num_kb)
    print(possible_paths_1)
    print("Possible Paths for Robot 2")

    for path_1 in possible_paths_1:
        for target_1 in path_1[1]:
            dir_1_pos = og_dir_1_pos  # Reset Robot 2 for each new direction it needs to input
            print(target_1)
            coord_2 = find_coord(dir_kb, target_1)
            possible_paths_2 = get_all_shortest_paths(dir_1_pos, coord_2, dir_kb)
            print(possible_paths_2)
            dir_1_pos = coord_2
            print("Possible Paths for Robot 3")

            for path_2 in possible_paths_2:
                print("---")
                dir_2_pos = og_dir_2_pos  # Reset Robot 3 once before executing all moves in path_2
                possible_paths_3 = []
                for target_2 in path_2[1]:
                    coord_3 = find_coord(dir_kb, target_2)
                    possible_paths_3.append(get_all_shortest_paths(dir_2_pos, coord_3, dir_kb)[0])
                    dir_2_pos = coord_3  # Update position for next move in sequence

                final_path = []
                for path in possible_paths_3:
                    final_path.append(path[1])
                    print("path", path)
                final_final_paths.append(flatten_list(final_path))

    print("FINAL")
    final_final_paths = [path for path in final_final_paths if path and path != ['A']]
    shortest_path = min(final_final_paths, key=len)
    print("Shortest path:", shortest_path)
    return(shortest_path)


def part_one(codes):
    global num_pos, dir_1_pos, dir_2_pos
    result = 0
    for code in codes:
        sequence = []
        for c in code:
            sequence += find_sequence(c)
            print("HELLLLOOOOOO")
            print(sequence)
            print(len(sequence))
        #print(sequence)
        print(len(sequence))
        code_int = int(''.join([i for i in code if i.isdigit()]))
        print(code_int)
        print(sequence)
        result += code_int * len(sequence)
    return result


def main():
    data = [list(line.strip()) for line in open(filename)]
    print('#1 -> ', part_one(data))

main()