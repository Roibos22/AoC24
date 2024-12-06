map = [list(line.strip()) for line in open('input_test.txt')]

# 1939
# 106 42

pos = [0, 0]
dir = None
directions = [
		['^', ( 0, -1), '|'],
		['>', ( 1,  0), '-'],
		['v', ( 0, +1), '|'],
		['<', (-1,  0), '-'],
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


find_pos(map)

def in_range(map, x, y):
	return (
		x >= 0 and\
		y >= 0 and\
		x <  len(map[0]) and\
		y < len(map)
	)

def is_visited(visited, pos):
	if tuple(pos) in visited:
		return True
	#elif pos[2] in 'v^><':

	else:
		print(pos[2])
		return False

def is_loop(map, pos, dir, x, y):
	global directions

	visited = set()

	if map[y][x] == '#':
		return 0

	map[y][x] = 'O'

	while(in_range(map, pos[0], pos[1])):

		# change direction if obstacle
		if in_range(map, pos[1] + dir[1][1], pos[0] + dir[1][0]):
			if map[pos[1] + dir[1][1]][pos[0] + dir[1][0]] in '#O':
				map[pos[1]][pos[0]] = '+'
				cur_i = directions.index(dir)
				next_i = (cur_i + 1) % len(directions)
				dir = directions[next_i]

		# mark position as visited
		if (map[pos[1]][pos[0]] == '-' or map[pos[1]][pos[0]] == '|'):
			map[pos[1]][pos[0]] = '+'
		elif map[pos[1]][pos[0]] == '.':
			map[pos[1]][pos[0]] = dir[2]

		# print(dir)
		# print(pos)
		# if in_range(map, pos[0] + dir[1][0], pos[1] + dir[1][1]):
		#     # print("next ", map[pos[1] + dir[1][1]][pos[0] + dir[1][0]], dir[2])
		#     # if(map[pos[1] + dir[1][1]][pos[0] + dir[1][0]] == dir[2] or map[pos[1] + dir[1][1]][pos[0] + dir[1][0]] == '+'):
		#     if(map[pos[1] + dir[1][1]][pos[0] + dir[1][0]] == '+'):
		#         print("next 2", map[pos[1] + 2*dir[1][1]][pos[0] + 2*dir[1][0]], dir[2])
		#         if(map[pos[1] + 2*dir[1][1]][pos[0] + 2*dir[1][0]] != '.'):
		#             print(pos, dir)
		#             print(map[pos[1] + dir[1][1]][pos[0] + dir[1][0]])
		#             for i, line in enumerate(map):
		#                 print(f"{i:2} ", end='')  # Row number with 2 spaces for alignment
		#                 print(''.join(line), end='\n\n')

		#             return 1

		# if next pos in visited return 1
		next_pos = [pos[0] + dir[1][0], pos[1] + dir[1][1], dir[0]]
		if (in_range(map, next_pos[0], next_pos[1])):
			print(next_pos[2], map[next_pos[1]][next_pos[0]])
		if (in_range(map, next_pos[0], next_pos[1]) and not is_visited(visited, next_pos)):
			visited.add(tuple(next_pos))
			# print(next_pos)
		elif(in_range(map, next_pos[0], next_pos[1])):
			print("reurned 1")
			for i, line in enumerate(map):
				print(f"{i:2} ", end='')  # Row number with 2 spaces for alignment
				print(''.join(line), end='\n\n')
			return 1

		# else add next pos to visited

		# move position
		pos[1] = pos[1] + dir[1][1]
		pos[0] = pos[0] + dir[1][0]
		# if in_range(map, pos[0], pos[1]):
		#     map[pos[0]][pos[1]] = dir[0]
		# print(pos)
		# for line in map:
		#     print(''.join(line), end='\n\n')
		# print("", end='\n\n')

	return 0

res2 = 0
for y in range(len(map)):
	for x in range(len(map[y])):
		# print(x, y)
		tmp_map = [row[:] for row in map]
		tmp_pos = pos[:]
		tmp_dir = dir[:]
		#print("dir:" ,tmp_dir)
		res2 += is_loop(tmp_map, tmp_pos, dir, x, y)

# tmp_map = [row[:] for row in map]
# tmp_pos = pos[:]
# tmp_dir = dir[:]
# res2 += is_loop(tmp_map, tmp_pos, dir, 106, 42)

# for line in map:
#     print(line)

print("#2 -> ", res2)


# [105, 43]
# [104, 43]
# [104, 42]
# [105, 42]