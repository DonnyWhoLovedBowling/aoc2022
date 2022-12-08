f = open('../data/ex8.txt')
lines = f.readlines()
lines = [line.replace('\n', '') for line in lines]
visible = [[False for c in line] for line in lines]

for x in range(0, len(lines)):
    highest_tree = -1
    line = lines[x]
    for y in range(0, len(line)):
        t = int(line[y])
        if t > highest_tree:
            visible[x][y] = True    # visible from left
            highest_tree = t
            if highest_tree == 9:
                break
    highest_tree = -1
    for y in range(len(line)-1, -1, -1):
        t = int(line[y])
        if t > highest_tree:
            visible[x][y] = True    # visible from right
            highest_tree = t
            if highest_tree == 9:
                break

for y in range(0, len(lines[0])):
    highest_tree = -1
    column = [i[y] for i in lines]
    for x in range(0, len(column)):
        t = int(column[x])
        if t > highest_tree:
            visible[x][y] = True    # visible from above
            highest_tree = t
            if highest_tree == 9:
                break
    highest_tree = -1
    for x in range(len(column)-1, -1, -1):
        t = int(column[x])
        if t > highest_tree:
            visible[x][y] = True    # visible from below
            highest_tree = t
            if highest_tree == 9:
                break

print(visible)
score = 0
for i in visible:
    for j in i:
        if j:
            score += 1
print(score)


def scenic_score(_x, _y):
    global lines
    col = [i[_y] for i in lines]
    row = lines[_x]
    height = int(lines[_x][_y])
    up = 0
    down = 0
    left = 0
    right = 0
    for i in range(_x - 1, -1, -1):
        up += 1
        if int(col[i]) >= height:
            break
    for i in range(_x + 1, len(row)):
        down += 1
        if int(col[i]) >= height:
            break
    for i in range(_y - 1, -1, -1):
        left += 1
        if int(row[i]) >= height:
            break
    for i in range(_y + 1, len(col)):
        right += 1
        if int(row[i]) >= height:
            break
    return up*down*left*right


max_score = 0
for i in range(0, len(lines)):
    for j in range(0, len(lines[i])):
        score = scenic_score(i, j)
        if score > max_score:
            max_score = score
print(max_score)
