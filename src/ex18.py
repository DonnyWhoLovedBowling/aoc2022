from collections import deque


def add_or_remove(p, points):
    if p in points:
        points.remove(c)
    else:
        points.add(c)


lines = open('../data/ex18.txt')
cubes = set()
data3d = []
score = 0
ixs = deque([0, 1, 2])
x_min, y_min, z_min = 50, 50, 50
x_max, y_max, z_max = 0, 0, 0
open_sides = set()
for line in lines:
    cube = eval('(' + line.replace('\n', '') + ')')
    x_min = min(x_min, cube[0]-1)
    y_min = min(y_min, cube[1]-1)
    z_min = min(z_min, cube[2]-1)
    x_max = max(x_max, cube[0]+1)
    y_max = max(y_max, cube[1]+1)
    z_max = max(z_max, cube[2]+1)
    cubes.add(cube)
    new = 6
    for i in [-.5, .5]:
        c = (cube[0] + i, cube[1], cube[2])
        add_or_remove(c, open_sides)
    for i in [-.5, .5]:
        c = (cube[0], cube[1] + i, cube[2])
        add_or_remove(c, open_sides)
    for i in [-.5, .5]:
        c = (cube[0], cube[1], cube[2] + i)
        add_or_remove(c, open_sides)

print(len(open_sides))

points_to_check = [(x_min, y_min, z_min)]
air = set()
counter = 0
while len(points_to_check) > 0:
    ptc = points_to_check.pop(0)
    if counter % 1000 == 0:
        print(counter, len(points_to_check))
    counter += 1
    if ptc in cubes or ptc in air:
        continue
    if x_min > ptc[0] or x_max < ptc[0] or y_min > ptc[1] or y_max < ptc[1] or z_min > ptc[2] or z_max < ptc[2]:
        continue
    air.add(ptc)
    for i in [-1, 1]:
        c = (ptc[0] + i, ptc[1], ptc[2])
        points_to_check.append(c)
    for i in [-1, 1]:
        c = (ptc[0], ptc[1] + i, ptc[2])
        points_to_check.append(c)
    for i in [-1, 1]:
        c = (ptc[0], ptc[1], ptc[2] + i)
        points_to_check.append(c)
relevant_sides = set()

for a in air:
    for i in [-.5, .5]:
        c = (a[0] + i, a[1], a[2])
        add_or_remove(c, relevant_sides)
    for i in [-.5, .5]:
        c = (a[0], a[1] + i, a[2])
        add_or_remove(c, relevant_sides)
    for i in [-.5, .5]:
        c = (a[0], a[1], a[2] + i)
        add_or_remove(c, relevant_sides)

ex_sides = open_sides.intersection(relevant_sides)
print(len(ex_sides))
