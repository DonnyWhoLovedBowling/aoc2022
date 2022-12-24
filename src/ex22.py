import regex as re


def cross_over(_x, _y, _d):
    global new_lines
    if _x == 149 and _d == 'r':  # 1 -> 4
        _d = 'l'
        _x = 99
        _y = 149 - _y
    elif _y == 0 and _x > 99 and _d == 'u':  # 1-> 6
        _d = 'u'
        _y = 199
        _x -= 100
    elif _y == 0 and 49 < _x < 100 and _d == 'u':  # 2 -> 6
        _d = 'r'
        _y = _x + 100
        _x = 0
    elif _x == 50 and _y < 50 and _d == 'l':  # 2 -> 5
        _d = 'r'
        _y = 149 - _y
        _x = 0
    elif _x == 50 and 49 < _y < 100 and _d == 'l':  # 3 -> 5
        _d = 'd'
        _x = _y - 50
        _y = 100
    elif _x < 50 and _y == 100 and _d == 'u':  # 5 -> 3
        _d = 'r'
        _y = _x + 50
        _x = 50
    elif _x == 0 and 99 < _y < 150 and _d == 'l':  # 5 -> 2
        _d = 'r'
        _y = 149 - _y  # 149 -> 0,100 -> 49
        _x = 50
    elif _x == 0 and _y > 149 and _d == 'l':  # 6 -> 2
        _d = 'd'
        _x = _y - 100
        _y = 0
    elif _x < 50 and _y == 199 and _d == 'd':  # 6 -> 1
        _d = 'd'
        _y = 0
        _x += 100  # 0 -> 100, 49 ->149
    elif _x == 49 and _y > 149 and _d == 'r':  # 6 -> 4
        _d = 'u'
        _x = _y - 100  # 150 -> 50, 199 -> 99
        _y = 149
    elif 49 < _x < 100 and _y == 149 and _d == 'd':  # 4 -> 6
        _d = 'l'
        _y = _x + 100
        _x = 49
    elif _x == 99 and 99 < _y < 150  and _d == 'r':  # 4 -> 1
        _d = 'l'
        _y = 149 - _y
        _x = 149
    elif _x == 99 and 49 < _y < 100 and _d == 'r':  # 3 -> 1
        _d = 'u'
        _x = _y + 50
        _y = 49
    elif 99 < _x < 150 and _y == 49 and _d == 'd':  # 1 -> 3
        _d = 'l'
        _y = _x - 50
        _x = 99
    else:
        raise RuntimeError('unknown cross-over')
    if new_lines[_y][_x] not in ['.','#']:
        raise RuntimeError('wrond cross-over')
    return _x, _y, _d


def rotate(_r, _d):
    if _d == '':
        return _r
    if _r == 'r':
        return 'd' if _d == 'R' else 'u'
    if _r == 'd':
        return 'l' if _d == 'R' else 'r'
    if _r == 'l':
        return 'u' if _d == 'R' else 'd'
    if _r == 'u':
        return 'r' if _d == 'R' else 'l'


lines = open('../data/ex22.txt').readlines()
moves = ''
x_lims = []
y_lims = dict()
new_lines = []
for y, line in enumerate(lines):
    line = line.replace('\n', '')
    indices = [i for i, j in enumerate(line) if j.strip()]
    if len(line) > 0 and line[0].isnumeric():
        moves = line
    elif len(indices) > 0 and line.strip() != '':
        x_lims.append((min(indices), max(indices)))
        new_lines.append(line)

x_lim_old = [99, -99]
for y, x_lim in enumerate(x_lims):
    if x_lim[0] < x_lim_old[0] and x_lim[1] > x_lim_old[1]:
        x_lim_old[0] = x_lim[0]
        x_lim_old[1] = x_lim[1]
        for x in range(x_lim[0], x_lim[1] + 1):
            y_lims[x] = [y]
    if x_lim[1] < x_lim_old[1]:
        for x in range(x_lim[1] + 1, x_lim_old[1] + 1):
            if x in y_lims:
                y_lims[x].append(y - 1)
    if x_lim[0] < x_lim_old[0]:
        for x in range(x_lim[0], x_lim_old[0]):
            y_lims[x] = [y]
    # only in test ...
    if x_lim[0] > x_lim_old[0]:
        for x in range(x_lim_old[0], x_lim[0]):
            y_lims[x].append(y - 1)
        for x in range(x_lim_old[1] + 1, x_lim[1] + 1):
            y_lims[x] = [y]

    x_lim_old[0] = x_lim[0]
    x_lim_old[1] = x_lim[1]

for k, v in y_lims.items():
    if len(v) == 1:
        y_lims[k].append(len(new_lines) - 1)
print(x_lims)
print(y_lims)

pos_x = new_lines[0].find('.')
pos_y = 0
r = 'r'
d = ''
while len(moves) > 0:
    match = re.search(r'\D', moves)
    if match:
        ix = match.start()
        m = int(moves[0:ix])
        d = moves[ix]
        moves = moves[ix + 1:]
    else:
        m = int(moves)
        moves = ''
        d = ''
    print(pos_y, pos_x, r)
    for step in range(0, m):
        last_x = pos_x
        last_y = pos_y
        last_r = r
        if r == 'r':
            if x_lims[pos_y][1] == pos_x:
                pos_x, pos_y, r = cross_over(pos_x, pos_y, r)
                # pos_x = x_lims[pos_y][0]
            else:
                pos_x += 1
        elif r == 'l':
            if x_lims[pos_y][0] == pos_x:
                pos_x, pos_y, r = cross_over(pos_x, pos_y, r)
                # pos_x = x_lims[pos_y][1]
            else:
                pos_x -= 1
        elif r == 'u':
            if y_lims[pos_x][0] == pos_y:
                pos_x, pos_y, r = cross_over(pos_x, pos_y, r)
                # pos_y = y_lims[pos_x][1]
            else:
                pos_y -= 1
        elif r == 'd':
            if y_lims[pos_x][1] == pos_y:
                pos_x, pos_y, r = cross_over(pos_x, pos_y, r)
                # pos_y = y_lims[pos_x][0]
            else:
                pos_y += 1
        try:
            v = new_lines[pos_y][pos_x]
        except IndexError as ie:
            print(ie)
        if v == '#':
            pos_x = last_x
            pos_y = last_y
            r = last_r
            break
    r = rotate(r, d)
# Facing is 0 for right (>), 1 for down (v), 2 for left (<), and 3 for up (^).
f = 0
if r == 'd':
    f = 1
elif r == 'l':
    f = 2
elif r == 'u':
    f = 3
print(pos_x, pos_y, r, f)
print(1000 * (pos_y + 1) + 4 * (pos_x + 1) + f)
