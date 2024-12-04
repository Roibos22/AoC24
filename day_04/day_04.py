data = []
str = "XMAS"

with open('input.txt', 'r') as file:
    data = [line.strip() for line in file]

# for i in range(len(data)):
#     print(data[i])

count = 0

def in_range(y, x):
    return (y >= 0 and y < len(data) and 
            x >= 0 and x < len(data[y]))

def check_xmas(y, x):
    global count

    if in_range(y - 1, x - 1) and data[y - 1][x - 1] == 'M':
       if in_range(y - 2, x - 2) and data[y - 2][x - 2] == 'A':
           if in_range(y - 3, x - 3) and data[y - 3][x - 3] == 'S':
               count += 1

    if in_range(y - 1, x) and data[y - 1][x] == 'M':
        if in_range(y - 2, x) and data[y - 2][x] == 'A':
            if in_range(y - 3, x) and data[y - 3][x] == 'S':
                count += 1
               
    if in_range(y - 1, x + 1) and data[y - 1][x + 1] == 'M':
        if in_range(y - 2, x + 2) and data[y - 2][x + 2] == 'A':
            if in_range(y - 3, x + 3) and data[y - 3][x + 3] == 'S':
                count += 1
               
    if in_range(y, x - 1) and data[y][x - 1] == 'M':
        if in_range(y, x - 2) and data[y][x - 2] == 'A':
            if in_range(y, x - 3) and data[y][x - 3] == 'S':
               count += 1
               
    if in_range(y, x + 1) and data[y][x + 1] == 'M':
        if in_range(y, x + 2) and data[y][x + 2] == 'A':
            if in_range(y, x + 3) and data[y][x + 3] == 'S':
                count += 1
               
    if in_range(y + 1, x - 1) and data[y + 1][x - 1] == 'M':
        if in_range(y + 2, x - 2) and data[y + 2][x - 2] == 'A':
            if in_range(y + 3, x - 3) and data[y + 3][x - 3] == 'S':
                count += 1
               
    if in_range(y + 1, x) and data[y + 1][x] == 'M':
       if in_range(y + 2, x) and data[y + 2][x] == 'A':
           if in_range(y + 3, x) and data[y + 3][x] == 'S':
               count += 1
               
    if in_range(y + 1, x + 1) and data[y + 1][x + 1] == 'M':
        if in_range(y + 2, x + 2) and data[y + 2][x + 2] == 'A':
            if in_range(y + 3, x + 3) and data[y + 3][x + 3] == 'S':
                count += 1


for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'X':
            # print(y , x)
            # check_char(y, x, 1)
            check_xmas(y, x)

print("#1 ->", count)
count = 0

def check_x_mas(y, x):
    global count

    # top two
    if in_range(y - 1, x - 1) and data[y - 1][x - 1] == 'M' and in_range(y - 1, x + 1) and data[y - 1][x + 1] == 'M':
        if in_range(y + 1, x - 1) and data[y + 1][x - 1] == 'S' and in_range(y + 1, x + 1) and data[y + 1][x + 1] == 'S':
            count += 1

    # left two
    if in_range(y - 1, x - 1) and data[y - 1][x - 1] == 'M' and in_range(y + 1, x - 1) and data[y + 1][x - 1] == 'M':
        if in_range(y - 1, x + 1) and data[y - 1][x + 1] == 'S' and in_range(y + 1, x + 1) and data[y + 1][x + 1] == 'S':
            count += 1

    #right two
    if in_range(y - 1, x + 1) and data[y - 1][x + 1] == 'M' and in_range(y + 1, x + 1) and data[y + 1][x + 1] == 'M':
        if in_range(y - 1, x - 1) and data[y - 1][x - 1] == 'S' and in_range(y + 1, x - 1) and data[y + 1][x - 1] == 'S':
            count += 1

    # bottom two
    if in_range(y + 1, x - 1) and data[y + 1][x - 1] == 'M' and in_range(y + 1, x + 1) and data[y + 1][x + 1] == 'M':
        if in_range(y - 1, x - 1) and data[y - 1][x - 1] == 'S' and in_range(y - 1, x + 1) and data[y - 1][x + 1] == 'S':
            count += 1


for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'A':
            check_x_mas(y, x)


print("#2 ->", count)
