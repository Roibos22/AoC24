import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def mix_and_prune(value, secret):
    secret = value ^ secret
    secret = secret % 16777216
    return secret

def get_next_price(secret):
    secret = mix_and_prune(secret * 64, secret)
    secret = mix_and_prune(int(secret / 32), secret)
    secret = mix_and_prune(secret * 2048, secret)
    return secret

def part_one(data, iterations):
    for _ in range(iterations):
        for secret in range(len(data)):
            data[secret] = get_next_price(data[secret])
    return(sum(secret for secret in data))

def get_prices(data, iterations):
    prices = []
    for monkey in range(len(data)):
        monkey_prices = []
        secret = data[monkey]
        monkey_prices.append(secret % 10)
        for _ in range(iterations):
            secret = get_next_price(secret)
            monkey_prices.append(secret % 10)
        prices.append(monkey_prices)
    return prices

def part_two(data, iterations):
    prices = get_prices(data, iterations)
    total_sequences = {}
    for monkey_prices in prices:
        seen = set()
        for i in range(len(monkey_prices) - 4):
            p1, p2, p3, p4, p5 = monkey_prices[i:i+5]
            sequence = (p2 - p1, p3 - p2, p4 - p3, p5 - p4)
            if sequence in seen: continue 
            seen.add(sequence)
            if sequence not in total_sequences:
                total_sequences[sequence] = 0
            total_sequences[sequence] += p5
    return max(total_sequences.values())

def main():
    data = [int(line.strip()) for line in open(filename)]
    print('#1 -> ', part_one(data, 2000))
    data = [int(line.strip()) for line in open(filename)]
    print('#2 -> ', part_two(data, 2000))

main()