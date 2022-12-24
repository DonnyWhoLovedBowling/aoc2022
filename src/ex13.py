import json
import functools
from copy import deepcopy


def compare(l1_orig, l2_orig):
    l1 = deepcopy(l1_orig)
    l2 = deepcopy(l2_orig)

    if len(l1) > 0 and len(l2) > 0:
        o1 = l1.pop(0)
        o2 = l2.pop(0)
        if type(o1) == list and type(o2) == list:
            comp = compare(o1, o2)
            if comp == -1:
                if len(o1) > 0 or len(o2) > 0:
                    return compare(o1, o2)
                else:
                    return compare(l1, l2)
            else:
                return comp
        elif type(o1) == list:
            return compare(o1, [o2])
        elif type(o2) == list:
            return compare([o1], o2)
        elif o1 == o2:
            return compare(l1, l2)
        else:
            return o2 > o1
    if len(l1) > 0:
        return False
    if len(l2) > 0:
        return True
    else:
        return -1


def wrapper(l1, l2):
    if compare(l1, l2):
        return -1
    else:
        return 1


def do_run(in_lines):
    ix = 0
    jx = 1
    l = [0, 0]
    score = 0
    new_lines = []
    for line in in_lines:
        if line.replace('\n', '') == '':
            jx += 1
            ix = 0
            continue
        l[ix] = json.loads(line)
        new_lines.append(deepcopy(l[ix]))
        ix += 1
        if ix == 2:
            c = compare(l[0], l[1])
            if c:
                score += jx

    print(score)
    return new_lines


lines = open('../data/ex13.txt', 'r').readlines()
new_lines = do_run(lines)
new_lines.append([[2]])
new_lines.append([[6]])


lines_sorted = sorted(new_lines, key=functools.cmp_to_key(wrapper))

print((lines_sorted.index([[6]])+1)*(lines_sorted.index([[2]])+1))
