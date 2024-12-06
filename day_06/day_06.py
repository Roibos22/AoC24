map = [list(line.strip()) for line in open('input.txt')]

pos = [0, 0]
dir = None
directions = [
        ['^', ( 0, -1)],
        ['>', ( 1,  0)],
        ['v', ( 0, +1)],
        ['<', (-1,  0)],
    ]

def find_pos(map):
    global pos, dir
    for y, line in enumerate(map):
        for x, char in enumerate(line):
            for d in directions:
                if d[0] == char:
                    dir = d
                    pos[0] = x
                    pos[1] = y
                    break
            # if char in ' <>^v':
            #     pos[0] = x
            #     pos[1] = y
            #     dir = map[y][x]
            #     return

find_pos(map)

def in_range(map, x, y):
    return (
        x >= 0 and\
        y >= 0 and\
        x <  len(map[0]) and\
        y < len(map)
    )

while(in_range(map, pos[0], pos[1])):

    # if map[pos[1] + dir[1][1]][pos[0] + dir[1][0]]
    print("y ", pos[1] + dir[1][1])
    print("x", pos[0] + dir[1][0])
    if in_range(map, pos[1] + dir[1][1], pos[0] + dir[1][0]):
        if map[pos[1] + dir[1][1]][pos[0] + dir[1][0]] == '#':
            cur_i = directions.index(dir)
            next_i = (cur_i + 1) % len(directions)
            dir = directions[next_i]

    map[pos[1]][pos[0]] = 'x'
    pos[1] = pos[1] + dir[1][1]
    pos[0] = pos[0] + dir[1][0]

res1 = sum(row.count('x') for row in map)

print("#1 -> ", res1)

    # match dir[0]:
    #     case '^':
    #         map[pos[1]][pos[0]] = 'x'
    #         pos[1] = pos[1] - 1


print(dir)
print(pos)

for line in map:
    print(line)