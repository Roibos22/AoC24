import sys

test = True if len(sys.argv) == 2 and sys.argv[1] == "test" else False
filename = "input_test.txt" if test else "input.txt"

def parse_data(filename):
    connections = []
    with open(filename) as file:
        for line in file:
            new = (line.strip()[:2], line.strip()[3:])
            connections.append(new)
    return connections

def prepare_data(data):
    connections = {}
    for cp1, cp2 in data:
        if cp1 not in connections:
            connections[cp1] = []
        connections[cp1].append(cp2)
        if cp2 not in connections:
            connections[cp2] = []
        connections[cp2].append(cp1)
    return connections

def part_one(connections):
    inter_connections_3 = set()
    for cp1, connected in connections.items():
        for cp2 in connected:
            for cp3 in connections[cp2]:
                if cp3 in connected:
                    inter_connections_3.add(tuple(sorted([cp1, cp2, cp3])))

    result = 0
    for connection in inter_connections_3:
        if any('t' in pc[0] for pc in connection):
            result += 1
    return result

def part_two(connections):
    networks = []
    map = {}
    for a, b in connections:
        map.setdefault(a, set()).add(b)
        map.setdefault(b, set()).add(a)

    for cp1, cp2 in connections:
        added = False
        for network in networks:
            if cp1 in network and cp2 not in network:
                if all(cp2 in map[cp] or cp is cp1 for cp in network):
                    network.append(cp2)
                    added = True
                    break
            elif cp2 in network and cp1 not in network:
                if all(cp1 in map[cp] or cp is cp2 for cp in network):
                    network.append(cp1)
                    added = True
                    break
        if not added:
            networks.append([cp1, cp2])

    return(",".join(sorted(max(networks, key=len))))

def main():
    data = parse_data(filename)
    connections = prepare_data(data)
    print("#1 -> ", part_one(connections))
    print("#2 -> ", part_two(data))

main()