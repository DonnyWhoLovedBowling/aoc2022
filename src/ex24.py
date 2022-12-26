import math
from copy import deepcopy as dc
import sys


def e_ok(e, _ls, _rs, _us, _ds):
    global hs, max_x, max_y
    ret_val = True
    if e[0] < 0 or e[1] < 0:
        ret_val = False
    elif e in _ls:
        ret_val = False
    elif e in _rs:
        ret_val = False
    elif e in _ds:
        ret_val = False
    elif e in _us:
        ret_val = False
    elif e in hs:
        ret_val = False
    return ret_val


def move_e(e, option):
    global max_x, max_y
    ret_val = dc(e)
    if option == 'd':
        ret_val = (e[0] + 1, e[1])
    elif option == 'u':
        ret_val = (e[0] - 1, e[1])
    elif option == 'l':
        ret_val = (e[0], e[1] - 1)
    elif option == 'r':
        ret_val = (e[0], e[1] + 1)
    return ret_val


def do_turn(_ls, _rs, _us, _ds):
    global hs, max_x, max_y
    __ls = set()
    __rs = set()
    __ds = set()
    __us = set()

    for y, x in _ls:
        if x == 1:
            __ls.add((y, max_x))
        else:
            __ls.add((y, x - 1))
    for y, x in _rs:
        if x == max_x:
            __rs.add((y, 1))
        else:
            __rs.add((y, x + 1))
    for y, x in _ds:
        if y == max_y:
            __ds.add((1, x))
        else:
            __ds.add((y + 1, x))
    for y, x in _us:
        if y == 1:
            __us.add((max_y, x))
        else:
            __us.add((y - 1, x))
    return __ls, __rs, __us, __ds


def min_rounds(start, end):
    q = [start]
    tot_dist = dict()
    tot_dist[start] = 0
    min_dist = -1
    global _ls, _rs, _us, _ds
    while q:
        old_key = q.pop(0)
        n_turns = tot_dist[old_key]
        n_turns_new = n_turns + 1
        n_turns_key = (old_key[2]+1) % mod
        __ls = _ls[n_turns_key]
        __rs = _rs[n_turns_key]
        __us = _us[n_turns_key]
        __ds = _ds[n_turns_key]
        options = 'rdwlu'
        possible_options = []
        _e = (old_key[0], old_key[1])
        for option in options:
            __e = move_e(dc(_e), option)
            if e_ok(__e, __ls, __rs, __us, __ds):
                possible_options += option

        for p in possible_options:
            __e = move_e(dc(_e), p)
            key = (*__e, n_turns_key)
            if key in tot_dist:
                continue
            if __e == end:
                min_dist = n_turns_new
                q = []
                break
            tot_dist[key] = n_turns_new
            q.append(key)
    return min_dist


test = False
if test:
    lines = open('../data/ex24_test.txt')
    max_y = 4
    max_x = 6
else:
    lines = open('../data/ex24.txt')
    max_y = 25
    max_x = 120

ls = set()
rs = set()
us = set()
ds = set()
hs = set()

E = (0, 1)
for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '#':
            hs.add((i, j))
        if c == '<':
            ls.add((i, j))
        if c == '>':
            rs.add((i, j))
        if c == '^':
            us.add((i, j))
        if c == 'v':
            ds.add((i, j))
        if i == 0 and c == '.':
            E = (i, j)
_ls = []
_rs = []
_us = []
_ds = []
mod = int(max_y * max_x / math.gcd(max_x, max_y))

for i in range(0, mod):
    _ls.append(ls)
    _rs.append(rs)
    _us.append(us)
    _ds.append(ds)
    ls, rs, us, ds = do_turn(ls, rs, us, ds)

first = min_rounds((*E, 0), (max_y + 1, max_x))
print(first)
new_start = (max_y + 1, max_x, first % mod)
new_end = (0, 1)
print(new_start, new_end)
second = min_rounds(new_start, new_end)
print(second)
new_start = (0, 1, (first + second) % mod)
new_end = (max_y + 1, max_x)
print(new_start, new_end)
third = min_rounds(new_start, new_end)

print(third)
