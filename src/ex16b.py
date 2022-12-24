from copy import deepcopy as dc


def is_right_sequence(actions):
    right_seq = ['DD', 'BB', 'JJ', 'HH',
                 'EE','CC']

    for i, a in enumerate(actions):
        if right_seq[i] != a:
            return False
    return True


def do_cycle(start, closed_valves, current_rate, minutes, total_flow):
    global valves, paths, max_flow, relevant_distances

    for v in closed_valves:
        new_closed_valves = dc(closed_valves)
        new_closed_valves.remove(v)
        d = relevant_distances[start][v]
        new_minutes = minutes + d + 1
        new_rate = current_rate+valves[v]
        new_total_flow = total_flow + ((d+1) * current_rate)
        for v2 in new_closed_valves:
            new_new_closed_valves = dc(new_closed_valves)
            new_new_closed_valves.remove(v2)
            d2 = relevant_distances[start][v2]
            new_total_flow = new_total_flow + ((d2 + 1) * current_rate)
            f = 0
            if new_minutes > 26:
                f = total_flow
            if len(new_closed_valves) == 0:
                f = new_total_flow + (26 - new_minutes) * new_rate
            if f > max_flow:
                print(f)
                max_flow = f
                continue
            if f > 0:
                continue
            do_cycle(v, new_closed_valves, new_rate, new_minutes, new_total_flow)


relevant_distances = dict()

lines = open('../data/ex16.txt', 'r').readlines()
start_rates = dict()
valves = dict()
relevant_valves = list()
paths = dict()
max_flow = 0
for line in lines:
    line = line.replace('\n', '')
    valve = line[6:8]
    splt = line.split('=')
    ix = splt[1].find(';')
    rate = int(splt[1][0:ix])
    valve_paths = splt[1].split('valve')[1]
    if valve_paths[0] == 's':
        valve_paths = valve_paths[2:]
    if ',' in valve_paths:
        valve_paths = valve_paths.split(', ')
    else:
        valve_paths = [valve_paths[1:]]
    valves[valve] = rate
    paths[valve] = valve_paths
    if rate > 0:
        relevant_valves.add(valve)

relevant_valves = sorted(relevant_valves, key=lambda x: valves[x], reverse=True)

for v1 in valves:
    relevant_distances[v1] = {v2: 1e9 for v2 in valves}
    relevant_distances[v1][v1] = 0
    for v2 in paths[v1]:
        relevant_distances[v1][v2] = 1

for v1 in valves:
    for v2 in valves:
        for v3 in valves:
            try:
                relevant_distances[v2][v3] = min(relevant_distances[v2][v3], relevant_distances[v2][v1] + relevant_distances[v1][v3])
            except KeyError as ke:
                print(ke)

do_cycle('AA', relevant_valves, 0, 0, 0, [])
print(max_flow)
