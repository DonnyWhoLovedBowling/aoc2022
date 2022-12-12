import json
from math import floor

f = open('../data/ex11.txt')
lines = f.readlines()
monkey_counter = dict()
decision_map = dict()
action_dict = dict()
op = dict()
test_num = dict()
op_num = dict()
op_old = dict()
monkey = 0
monkeys = list()

for line in [line.replace('\n', '') for line in lines]:
    if not line:
        continue
    if line[0:6] == 'Monkey':
        monkey = int(line.split(' ')[1][0])
        monkeys.append(monkey)
    elif '  Starting items:' in line:
        start_list = json.loads('[' + line[18:] + ']')
        action_dict[monkey] = start_list
    elif 'Operation: new = old' in line:
        if line[24:].strip().isnumeric():
            op_num[monkey] = int(line[24:])
            op_old[monkey] = False
        else:
            op_old[monkey] = True
        op[monkey] = line[23]
    elif 'Test: divisible by' in line:
        test_num[monkey] = int(line[21:])
    elif 'true' in line:
        decision_map[monkey] = dict()
        decision_map[monkey][True] = int(line[-1])
    elif 'false' in line:
        decision_map[monkey][False] = int(line[-1])

ex = 'b'
end = 20 if ex == 'a' else 10000
tot_mod = 1
for num in test_num.values():
    tot_mod *= num

for play_round in range(0, end):
    debug = True
    if play_round % 50 == 0:
        print(play_round)
    for monkey in monkeys:
        for old in list(action_dict[monkey]):
            if op_old[monkey]:
                op_num[monkey] = old
            if op[monkey] == '+':
                new = old + op_num[monkey]
            else:
                new = old * op_num[monkey]
            if ex == 'a':
                new = floor(new/3)
            test = ((new % test_num[monkey]) == 0)
            new_monkey = decision_map[monkey][test]
            action_dict[new_monkey].append(new % tot_mod)
            if monkey in monkey_counter.keys():
                monkey_counter[monkey] += 1
            else:
                monkey_counter[monkey] = 1
        action_dict[monkey] = []
vals = list(monkey_counter.values())
vals.sort()
print(monkey_counter)
print(vals[-1]*vals[-2])





