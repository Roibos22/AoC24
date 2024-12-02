def is_sorted(arr):
    if all(arr[i] > arr[i + 1] for i in range(len(arr) - 1)):
        return True
    if all(arr[i] < arr[i + 1] for i in range(len(arr) - 1)):
        return True
    return False

def has_correct_differences(arr):
    return all(1 <= abs(arr[i] - arr[i + 1]) <= 3 for i in range(len(arr) - 1))

# PART 1

safe_files = 0

with open('input.txt', 'r') as file:
    for line in file:
        arr = line.strip().split()
        arr = [int(x) for x in arr]
        if is_sorted(arr) and has_correct_differences(arr):
            safe_files += 1

print('#1 -> ', safe_files)

# PART 2

safe_files = 0

with open('input.txt', 'r') as file:
    for line in file:
        arr = line.strip().split()
        arr = [int(x) for x in arr]
        for i in range(len(arr)):
            tmp = list(arr)
            tmp.pop(i)
            if is_sorted(tmp) and has_correct_differences(tmp):
                safe_files += 1
                break

print('#2 -> ', safe_files)
