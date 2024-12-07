import sys

def parse_input(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            numbers = line.split()
            result = int(numbers[0].strip(':'))
            numbers = [int(x) for x in numbers[1:]]
            data.append((result, numbers, []))
    return data

def evaluate_equation(data):
    if len(data[1]) is not len(data[2]) + 1:
        return False

    nums = data[1]
    result = nums[0]

    for i in range(len(data[2])):
        if data[2][i] == '+':
            result += nums[i + 1]
        elif data[2][i] == '*':
            result *= nums[i + 1]
        elif data[2][i] == '||':
            result = int(str(result) + str(nums[i + 1]))
    if test:
        print(data, result)

    return result == data[0]

def find_correct_operators(data, operators):

    def backtrack(pos, operators):
        if pos >= len(data[2]):
            return int(data[0]) if evaluate_equation(data) else 0

        operator = data[2][pos]

        for operator in operators:
            data[2][pos] = operator
            res = backtrack(pos + 1, operators)
            if res: return res

        data[2][pos] = operator
        return 0

    for i in range(len(data[1])  - 1):
        data[2].append("+") 
    return backtrack(0, operators)

def sum_results(filename, operators):
    data = parse_input(filename)
    sum = 0
    for i in range(len(data)):
        sum += find_correct_operators(data[i], operators)
    return sum

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False

def main():
    filename = "input_test.txt" if test else "input.txt"
    print("#1 -> ", sum_results(filename, ['+', '*']))
    print("#2 -> ", sum_results(filename, ['+', '*', '||']))

main()