# PART 1

left_list, right_list = [], []

with open('input.txt', 'r') as input_file:
    for line in input_file:
        left_num, right_num = line.split()
        left_list.append(int(left_num))
        right_list.append(int(right_num))

left_list.sort()
right_list.sort()

distance = 0
for left_num, right_num in zip(left_list, right_list):
    distance += abs(left_num - right_num)

print("#1 -> ", distance)

# PART 2

similarity_score = 0
for num in left_list:
    similarity_score += (num * right_list.count(num))

print("#2 -> ", similarity_score)
