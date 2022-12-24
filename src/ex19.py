import datetime
from copy import deepcopy as dc
import math
import re

n_turns = 32


def skip_option(option, current_inventory, current_robots, _costs, turns_left):
    global max_ore
    if option != 'geode':
        geode_possible = (current_inventory['ore'] > _costs['geode']['ore']) and \
                         (current_inventory['obsidian'] > _costs['geode']['obsidian'])
        if geode_possible:
            return True
    if option == 'ore':
        return (turns_left < (_costs['ore']['ore'] * 2)) or (current_robots['ore'] >= max_ore)
        # return (current_robots['ore'] >= max_ore)
    if option == 'clay':
        # t_until_obsid = (_costs['obsidian']['clay'] - current_inventory['clay'])
        # inv_obsid = current_inventory['obsidian'] + (current_robots['obsidian'] * t_until_obsid)
        # t_until_geode = _costs['geode']['obsidian'] - inv_obsid
        # return  (turns_left < t_until_geode) \
        return current_robots['clay'] >= costs['obsidian']['clay'] \
            #    or (turns_left <
            # math.ceil((_costs['obsidian']['clay'] - current_inventory['clay']) /
            #           (current_robots['clay'] + 1)))
    if option == 'obsidian':
        return (current_robots['obsidian'] >= costs['geode']['obsidian']) \
            #    or (turns_left <
            # math.ceil((_costs['geode']['obsidian'] - current_inventory['obsidian']) /
            #           (current_robots['obsidian'] + 1)))


def next_turn(i, current_robots, current_inventory, _costs):
    key = (i, *current_robots.values(), *current_inventory.values())
    if key in memory:
        return memory[key]
    max_geodes = 0
    for option in current_inventory.keys():
        if skip_option(option, current_inventory, current_robots, _costs, (n_turns - i)):
            continue
        _robots = dc(current_robots)
        _inventory = dc(current_inventory)

        if option in ['ore', 'clay']:
            turns = max(0, math.ceil((_costs[option]['ore'] - _inventory['ore']) / _robots['ore']))
        elif option == 'obsidian':
            if _robots['clay'] == 0:
                continue
            turns_ore = math.ceil((_costs[option]['ore'] - _inventory['ore']) / _robots['ore'])
            turns_clay = math.ceil((_costs[option]['clay'] - _inventory['clay']) / _robots['clay'])
            turns = max(turns_clay, turns_ore, 0)
        else:
            if _robots['obsidian'] == 0:
                continue
            turns_ore = math.ceil((_costs[option]['ore'] - _inventory['ore']) / _robots['ore'])
            turns_obs = math.ceil((_costs[option]['obsidian'] - _inventory['obsidian']) / _robots['obsidian'])
            turns = max(turns_obs, turns_ore, 0)
        turns += 1  # 1 om daadwerkelijk een robot te bouwen.
        new_i = i + turns
        do_option = True
        if new_i > n_turns:
            if i + 1 <= n_turns:
                new_i = i + 1
                turns = 1
                do_option = False
            else:
                continue

        for k, v in _robots.items():
            _inventory[k] += v * turns
        if do_option:
            _robots[option] += 1
            _inventory['ore'] -= _costs[option]['ore']
            if option == 'obsidian':
                _inventory['clay'] -= _costs[option]['clay']
            if option == 'geode':
                _inventory['obsidian'] -= _costs[option]['obsidian']
        max_geodes = max(max_geodes, _inventory['geode'])
        max_geodes = max(max_geodes, next_turn(new_i, _robots, _inventory, _costs))
    memory[key] = max_geodes
    return max_geodes


a = 'prod'
blueprints = []
costs = dict()
costs['ore'] = dict()
costs['clay'] = dict()
costs['obsidian'] = dict()
costs['geode'] = dict()

if a == 'test':
    lines = open('../data/ex19_test.txt').readlines()
    for line in lines:
        line = line[7:]
        robot = line.split(' robot')[0]
        cost1_ix = line.find('costs') + 6
        costs[robot] = {'ore': int(line[cost1_ix])}
        if 'obsidian' in robot:
            cost2_ix = line.find('and') + 4
            if line[cost2_ix + 1].isnumeric():
                costs[robot]['clay'] = int(line[cost2_ix:cost2_ix + 2])
            else:
                costs[robot]['clay'] = int(line[cost2_ix])

        if 'geode' in robot:
            cost2_ix = line.find('and') + 4
            if line[cost2_ix + 1].isnumeric():
                costs[robot]['obsidian'] = int(line[cost2_ix:cost2_ix + 2])
            else:
                costs[robot]['obsidian'] = int(line[cost2_ix])
    blueprints.append(dc(costs))

else:
    lines = open('../data/ex19.txt').readlines()
    for line in lines:
        nums = re.findall(r'\d+', line)
        costs['ore']['ore'] = int(nums[1])
        costs['clay']['ore'] = int(nums[2])
        costs['obsidian']['ore'] = int(nums[3])
        costs['obsidian']['clay'] = int(nums[4])
        costs['geode']['ore'] = int(nums[5])
        costs['geode']['obsidian'] = int(nums[6])
        blueprints.append(dc(costs))

score = 1
for ix, bp in enumerate(blueprints, 1):
    print(datetime.datetime.now())

    if ix > 3:
        continue
    max_ore = 0
    for r in bp:
        if r == 'ore':
            continue
        max_ore = max(max_ore, bp[r]['ore'])
    inventory = {ore: 0 for ore in bp.keys()}
    robots = {ore: 0 for ore in bp.keys()}
    robots['ore'] = 1
    memory = dict()
    mg = next_turn(0, robots, inventory, bp)
    score *= mg
    # score += ix*mg
    print(ix, mg, score)

print('score = ', score)
