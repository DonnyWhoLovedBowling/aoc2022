f = open('../data/ex14.txt')
lines = f.readlines()
graph = dict()
start = (500, 0)
end = 0
rocks = set()
sands = set()
bottom = 0

x_min = 1000
x_max = 0

for line in lines:
    sections = line.split('->')
    for i in range(0, len(sections)-1):
        ll, lr = sections[i].split(',')
        x1 = int(ll)
        y1 = int(lr)
        ll, lr = sections[i+1].split(',')
        x2 = int(ll)
        y2 = int(lr)
        if max(y1, y2) > bottom:
            bottom = max(y1, y2)
        if max(x1, x2) > x_max:
            x_max = max(x1, x2)
        if min(x1, x2) < x_min:
            x_min = min(x1, x2)

        if x1 == x2:
            for p in range(min(y1, y2), max(y1, y2)+1):
                rocks.add((x1, p))
        else:
            for p in range(min(x1, x2), max(x1, x2)+1):
                rocks.add((p, y1))

for p in range(x_min-200, x_max+200):
    rocks.add((p, bottom+2))

bottom += 2
sand = start
new_sand = sand
while True:
    if sand in sands:
        break
    while True:
        new_sand = (sand[0], sand[1]+1)
        if new_sand in rocks:
            new_sand = (sand[0]-1, sand[1]+1)
            if new_sand in rocks:
                new_sand = (sand[0]+1, sand[1]+1)
                if new_sand in rocks:
                    if sand in sands:
                        break
                    sands.add(sand)
                    rocks.add(sand)
                    sand = start
                    break
                else:
                    sand = new_sand
            else:
                sand = new_sand
        else:
            sand = new_sand
        if sand[1] >= bottom:
            break
    if new_sand[1] >= bottom and new_sand not in rocks:
        break

print(len(sands))
