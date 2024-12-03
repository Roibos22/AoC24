import re

res1 = 0
res2 = 0
enabled = True

def is_valid_mul(index, line):
    pattern = r'^mul\((\d+),(\d+)\)'
    match = re.search(pattern, line[index:])
    if match:
        return int(match.group(1)) * int(match.group(2))
    return 0

def check_enabled(index, line):
    old_enabled = enabled
    if re.search(r'^do\(\)', line[index:]):
        return True
    if re.search(r'^don\'t\(\)', line[index:]):
        return False
    return old_enabled

with open('input.txt', 'r') as file:
    for line in file:
        for index, char in enumerate(line):
            res1 += is_valid_mul(index, line)
            enabled = check_enabled(index, line)
            if enabled:
                res2 += is_valid_mul(index, line)

print("#1 ->", res1)
print("#2 ->", res2)

