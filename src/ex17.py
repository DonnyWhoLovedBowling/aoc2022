from copy import deepcopy as dc


def visualize(_points, _h):
    end_list = []
    for i in range(0, _h + 1):
        _l = ''
        for j in range(0, 7):
            if (j, i) in _points:
                _l += '#'
            else:
                _l += '.'
        end_list.append(_l)
    end_list.reverse()
    for _l in end_list:
        print(_l)


def move_rock(_r, d):
    __r = set()
    ok = True
    if d == '<':
        for x, y in _r:
            if x - 1 < 0:
                ok = False
                break
            __r.add((x - 1, y))
    elif d == '>':
        for x, y in _r:
            if x + 1 > 6:
                ok = False
                break
            __r.add((x + 1, y))
    elif d == 'v':
        for x, y in _r:
            __r.add((x, y - 1))

    return ok, __r


rocks = []
rock1 = {(2, 0), (3, 0), (4, 0), (5, 0)}
rock2 = {(3, 0), (2, 1), (4, 1), (3, 2)}
rock3 = {(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)}
rock4 = {(2, 0), (2, 1), (2, 2), (2, 3)}
rock5 = {(2, 0), (2, 1), (3, 0), (3, 1)}

rocks.append(rock1)
rocks.append(rock2)
rocks.append(rock3)
rocks.append(rock4)
rocks.append(rock5)

winds = open('../data/ex17.txt').read().replace('\n', '').strip()
winds_input = dc(winds)
highest = 0
rock_ix = 0
counter = 1000000000000
# counter = 2022
points = {(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0)}
i_counter = 0
last_counter = 0
last_highest = 0
resets = 0
while counter > 0:
    r = rocks[rock_ix]
    r = [(x, y + highest + 4) for x, y in r]
    period_found = True
    while True:
        w = winds[0]
        winds = winds[1:]
        if len(winds) == 0:
            winds = dc(winds_input)

        accept, new_r = move_rock(r, w)
        if accept and new_r.isdisjoint(points):
            r = new_r
        else:
            debug = 3
        accept, new_r = move_rock(r, 'v')
        if not new_r.isdisjoint(points):
            rock_ix += 1
            rock_ix = rock_ix % 5
            points = points.union(r)
            h = max([y for x, y in r])
            highest = max(highest, h)
            i_counter += 1
            if i_counter % 10000 == 0:
                # visualize(points, highest+5)
                # print(i_counter, highest, len(points), highest/i_counter)
                d = 6
                # points = {(x,y) for (x,y) in points if y > (highest-200)}
            counter -= 1
            break
        else:
            r = new_r
    if i_counter % 35 == 0:
        print(highest, i_counter - last_counter, highest - last_highest)
        last_counter = i_counter
        last_highest = highest
    if i_counter == 1180:
        print(highest)
        break

print(counter, highest)
