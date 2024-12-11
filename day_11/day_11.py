import sys
from functools import cache

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def part_one(data, loops):
    for i in range(loops):
        new_data = []
        for num in data:
            if num == 0:
                new_data.append(1)
            elif len(str(num)) % 2 == 0:
                middle = int(len(str(num)) / 2)
                new_data.append(int(str(num)[:middle]))
                new_data.append(int(str(num)[middle:]))
            else:
                new_data.append(num * 2024)
        data = new_data
    return (len(data))

@cache
def blink(stone, loops):
    if loops == 0:
        return 1
    if stone == 0:
        return blink(1, loops - 1)
    if (len(str(stone)) % 2 == 0):
        stone_str = str(stone)
        mid = int(len(stone_str) / 2)
        return (
            blink(int(stone_str[:mid]), loops - 1) +\
            blink(int(stone_str[mid:]), loops - 1)
        )
    return blink(stone * 2024, loops - 1)

def part_two(stones, loops):
    res = 0
    for stone in stones:
        res += blink(stone, loops)
    return res

def main():
    data = [int(x) for x in open(filename).readline().split()]
    print("#1 -> ", part_one(data, 25))
    print("#2 -> ", part_two(data, 75))
main()