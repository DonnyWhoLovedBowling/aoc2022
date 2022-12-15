from copy import deepcopy as dc
test = False
if test:
    f = open('../data/ex15_test.txt')
    n = 10
else:
    f = open('../data/ex15.txt')
    n = 2000000

lines = f.readlines()
input_map = dict()
excluded_set = set()
for line in lines:
    sx = int(line.split(':')[0].split(', ')[0].replace('Sensor at x=', ''))
    sy = int(line.split(':')[0].split('y=')[1])
    bx = int(line.split(':')[1].split(', ')[0].replace(' closest beacon is at x=', ''))
    by = int(line.split(':')[1].split('y=')[1])
    input_map[(sx, sy)] = (bx, by)
print(input_map)
beacons = set(input_map.values())

i = 0
range_map = dict()
for s, b in input_map.items():
    print(i)
    i += 1
    debug = s == (8, -7)
    dist = abs(s[0] - b[0]) + abs(s[1] - b[1])
    if debug:
        print(dist)
    for y in range((s[1] - dist), s[1] + dist):
        n_row = (dist - abs(y - s[1])) + 1
        if debug:
            print(y, n_row)
        if y in range_map.keys():
            range_map[y].append(range((s[0] - n_row) + 1, s[0] + n_row))
        else:
            range_map[y] = [range((s[0] - n_row) + 1, s[0] + n_row)]

l = set()
for r in range_map[n]:
    l = l.union(set(r))

for b in beacons:
    if b[1] == n:
        if b[0] in l:
            l.remove(b[1])

# answer ex a
print(len(l))

# ex b:

xmin = 0
ymin = 0

if test:
    xmax = 20
    ymax = 20
else:
    xmax = 4000000
    ymax = 4000000

x = range(xmin, xmax + 1)
free_map = dict()
for y in range_map.keys():
    if y % 100000 == 0:
        print('checking: ' + str(y))
    if y > ymax or y < ymin:
        continue
    free_map[y] = [x]
    for _range in range_map[y]:
        for fr in dc(free_map[y]):
            new_free = []
            if fr.start < _range.start and fr.stop > _range.stop:  # hash-range is in middle of free-range, cut up
                new_free.append(range(fr.start, _range.start))
                new_free.append(range(_range.stop, fr.stop))
            elif fr.stop <= _range.start:  # no overlap, free range left of hash-range
                continue
            elif fr.start >= _range.stop:  # no overlap, free range right of hash-range
                continue
            elif fr.start < _range.start < fr.stop:  # hash-range has overlap at right side of free-range
                new_free.append(range(fr.start, _range.start))
            elif fr.start < _range.stop < fr.stop:  # hash-range has overlap at left side of free-range
                new_free.append(range(_range.stop, fr.stop))
            free_map[y].remove(fr)
            free_map[y] += new_free
        if len(free_map[y]) == 0:
            break
    if len(free_map[y]) > 0:
        break
    else:
        del free_map[y]

print(free_map)
for k, v in free_map.items():
    if len(v) > 0:
        print(v[0].start*4000000+k)
