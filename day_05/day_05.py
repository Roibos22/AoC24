rules = []
orders = []
correct_orders = []
false_orders = []
correct_orders_middle_page_sum = 0
corrected_orders_middle_page_sum = 0

with open("input.txt", 'r') as file:
    for line in file:
        line = line.strip()
        if not line:
            break
        rules.append((line.strip().split('|')[0], line.strip().split('|')[1]))
    for line in file:
        line = line.strip()
        if not line:
            break
        orders.append(line.split(','))

def find_index(page, order):
    for i in range(len(order)):
        if page == order[i]:
            return i
    return None

def order_follows_rules(order, rules):
    for rule in rules:
        index_rule_0 = find_index(rule[0], order)
        index_rule_1 = find_index(rule[1], order)
        if index_rule_0 is not None and index_rule_1 is not None:
            if index_rule_0 > index_rule_1:
                return False
    return True

# PART 1

for order in orders:
    if order_follows_rules(order, rules):
        correct_orders.append(order)
        correct_orders_middle_page_sum += int(order[int(len(order) / 2)])
    else:
        false_orders.append(order)

# PART 2

for order in false_orders:
    while not order_follows_rules(order, rules):
        for rule in rules:
            index_rule_0 = find_index(rule[0], order)
            index_rule_1 = find_index(rule[1], order)
            if index_rule_0 is not None and index_rule_1 is not None:
                if index_rule_0 > index_rule_1:
                    order[index_rule_0], order[index_rule_1] = order[index_rule_1], order[index_rule_0]
    corrected_orders_middle_page_sum += int(order[int(len(order) / 2)])

print("#1 -> ", correct_orders_middle_page_sum)
print("#2 -> ", corrected_orders_middle_page_sum)