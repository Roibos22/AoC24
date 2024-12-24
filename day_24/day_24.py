import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def parse_data(filename):
    gates = [] # (wire1, operator, wire2, wire3)
    wires= {} # (wire, value)
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "":
                break
            wires[line[:3]] = int(line[5:])
        for line in file:
            line = line.strip().split()
            gates.append((line[0], line[1], line[2], line[4]))
    return wires, gates

def get_wire_value(wire, wires, gates):
    gate = next((gate for gate in gates if gate[3] == wire), None)
    wire_1_value = wires.get(gate[0]) if gate[0] in wires else get_wire_value(gate[0], wires, gates)
    wire_2_value = wires.get(gate[2]) if gate[2] in wires else get_wire_value(gate[2], wires, gates)

    if gate[1] == 'AND':
        return 1 if wire_1_value == wire_2_value == 1 else 0
    if gate[1] == 'OR':
        return 1 if wire_1_value == 1 or wire_2_value == 1 else 0
    if gate[1] == 'XOR':
        return 1 if wire_1_value != wire_2_value else 0

def part_one(wires, gates):
    for gate in gates:
        wires[gate[3]] = get_wire_value(gate[3], wires, gates)
    z_wires = reversed(sorted([wire for wire in wires if wire[0] == 'z']))
    number_binary = "".join([str(wires[wire]) for wire in z_wires])
    return int(number_binary, 2)

def main():
    wires, gates = parse_data(filename)
    print("#1 -> ", part_one(wires, gates))
    #print("#2 -> ", part_two())

main()