import datetime
from collections import deque


def move_elf(elf_pos, elves, dirs):
    y_o = elf_pos[0]
    x_o = elf_pos[1]

    skip_move = True
    for x in range(-1, 2):
        for y in range(-1, 2):
            if x == 0 and y == 0:
                continue
            skip_move = (y + y_o, x + x_o) not in elves
            if not skip_move:
                break
        if not skip_move:
            break
    if skip_move:
        ret_val = elf_pos
    else:
        ret_val = ''
        for d in dirs:
            if ret_val != '':
                break
            if d == 'N':
                if (y_o - 1, x_o - 1) in elves:
                    continue
                if (y_o - 1, x_o) in elves:
                    continue
                if (y_o - 1, x_o + 1) in elves:
                    continue
                ret_val = y_o - 1, x_o
            elif d == 'S':
                if (y_o + 1, x_o - 1) in elves:
                    continue
                if (y_o + 1, x_o) in elves:
                    continue
                if (y_o + 1, x_o + 1) in elves:
                    continue
                ret_val = y_o + 1, x_o
            elif d == 'W':
                if (y_o - 1, x_o - 1) in elves:
                    continue
                if (y_o, x_o - 1) in elves:
                    continue
                if (y_o + 1, x_o - 1) in elves:
                    continue
                ret_val = y_o, x_o - 1
            elif d == 'E':
                if (y_o - 1, x_o + 1) in elves:
                    continue
                if (y_o, x_o + 1) in elves:
                    continue
                if (y_o + 1, x_o + 1) in elves:
                    continue
                ret_val = y_o, x_o + 1
    return ret_val


def draw(elves):
    x_min = 100
    x_max = 0
    y_min = 100
    y_max = 0

    for elf in elves:
        x_min = min(elf[1], x_min)
        y_min = min(elf[0], y_min)
        x_max = max(elf[1], x_max)
        y_max = max(elf[0], y_max)

    for y in range(0, (y_max - y_min) + 1):
        l_str = ''
        for x in range(0, (x_max - x_min) + 1):
            if (y + y_min, x + x_min) in elves:
                l_str += '#'
            else:
                l_str += '.'
        print(l_str)
    return ((1 + x_max - x_min) * (1 + y_max - y_min)) - len(elves)


lines = open('../data/ex23.txt').readlines()
elves_ordered = []

directions = deque(['N', 'S', 'W', 'E'])

for i, line in enumerate(lines):
    line = line.replace('\n', '').strip()
    for j, c in enumerate(line):
        if c == '#':
            elves_ordered.append((i, j))

draw(set(elves_ordered))
print()
# for t in range(0, 10):

turns = 1
changed = 0
while True:
    if turns % 10 == 0:
        print(turns, changed, datetime.datetime.now())
    changed = 0

    new_positions_dict = dict()
    new_positions_set = set()
    dups = set()
    for i, e in enumerate(elves_ordered):
        new_pos = move_elf(e, elves_ordered, directions)
        if new_pos != e:
            changed += 1
            if new_pos in new_positions_set:
                dups.add(new_pos)
            elif new_pos:
                new_positions_set.add(new_pos)
                new_positions_dict[i] = new_pos

    for k, v in new_positions_dict.items():
        if v in dups:
            continue
        elves_ordered[k] = v
    # draw(set(elves_ordered))
    directions.rotate(-1)
    # print(directions)
    if changed == 0:
        break
    turns += 1


print(draw(set(elves_ordered)))
print(turns)