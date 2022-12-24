from copy import deepcopy


def make_list(ixmap):
    ret_val = []
    global lst
    for ii in range(0, len(lst)):
        ret_val.append(lst[ixmap[ii]])
    return ret_val


lines = open('../data/ex20.txt')
lst = []
for line in lines:
    lst.append(int(line.replace('\n', ''))*811589153)
original_lst = deepcopy(lst)
ix_map = dict()
reverse_ix_map = dict()
print(len(lst))
for i in range(0, len(lst)):
    ix_map[i] = i
    reverse_ix_map[i] = i

for i in range(0,10):
    for i in range(0, len(lst)):
        l = original_lst[i]
        if l == 0:
            print(l, ' found!')
            continue
        _ix_map = deepcopy(ix_map)
        _reverse_ix_map = deepcopy(reverse_ix_map)
        ix = ix_map[i]
        new_pos = (ix + l % (len(lst)-1))
        if new_pos < 0:
            new_pos = (new_pos % len(lst)) - 1
        elif new_pos >= len(lst):
            new_pos = (new_pos % len(lst)) + 1
        if ix == new_pos:
            print('ix == new_pos:', ix, l)
            continue
        ix_map[i] = new_pos
        reverse_ix_map[new_pos] = i

        if new_pos > ix:
            for j in range(ix+1, new_pos+1):
                k = _reverse_ix_map[j]
                dum = _ix_map[k]
                ix_map[k] -= 1
                reverse_ix_map[dum-1] = k
        elif new_pos < ix:
            for j in range(new_pos, ix):
                k = _reverse_ix_map[j]
                dum = _ix_map[k]
                ix_map[k] += 1
                reverse_ix_map[dum+1] = k


new_list = make_list(reverse_ix_map)

ix = new_list.index(0)
l1 = new_list[(ix + 1000) % len(lst)]
l2 = new_list[(ix + 2000) % len(lst)]
l3 = new_list[(ix + 3000) % len(lst)]

print(l1, l2, l3)
print(sum([l1, l2, l3]))
