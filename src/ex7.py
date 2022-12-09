lines = open('../data/ex7.txt', 'r').readlines()
dir_size_map = dict()
parent_map = dict()


def add_to_parents(size, cur_dir):
    parent = parent_map[cur_dir]
    if parent == '':
        return
    dir_size_map[parent] += size
    try:
        add_to_parents(size, parent)
    except RecursionError as e:
        print('recursion error at: ' + cur_dir + ' ' + parent)
    return


def dir_size(cur_dir):
    global lines
    global parent_map
    if len(lines) == 0:
        return
    if 'cd' not in lines[0]:
        print(lines[0])
        raise ValueError('cd not found!')
    if '..' in lines[0]:
        lines.pop(0)
        if cur_dir != '':
            dir_size(parent_map[cur_dir])
    if len(lines) == 0:
        return

    dum = cur_dir
    cur_dir = dum+'_'+lines[0].replace('$ cd ', '').replace('\n', '')
    if cur_dir not in parent_map.keys():
        parent_map[cur_dir] = dum
    if cur_dir not in dir_size_map.keys():
        dir_size_map[cur_dir] = 0
    lines.pop(0)
    if 'ls' not in lines[0]:
        raise ValueError('cd not found!')
    lines.pop(0)
    i = 0
    for line in lines:
        if 'dir' in line:
            i += 1
            continue
        elif line[0].isnumeric():
            i += 1
            size = int(line.split(' ')[0])
            dir_size_map[cur_dir] += size
            add_to_parents(size, cur_dir)
        else:
            break
    lines = lines[i:]
    if len(lines) > 0:
        dir_size(cur_dir)
    else:
        return


dir_size('')
print(dir_size_map)
# print(parent_map)

filtered_dict = {k: v for k, v in dir_size_map.items() if v <= 100000}
print(filtered_dict)
total = 0
for k, v in filtered_dict.items():
    total += v
print(total)

unused = 70000000 - dir_size_map['_/']
oke_dirs = [v for v in dir_size_map.values() if v >= (30000000 - unused)]
print(oke_dirs)
print(min(oke_dirs))


