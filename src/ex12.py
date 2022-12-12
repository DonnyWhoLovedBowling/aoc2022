def find_path(_graph, _start, _end):
    q = [_start]
    tot_dist = dict()
    tot_dist[_start] = 0
    ret_val = 0
    while q:
        i = q.pop(0)
        d = tot_dist[i]
        for k, v in _graph[i].items():
            if k in tot_dist:
                continue
            new_distance = d + 1
            if k == _end:
                ret_val = new_distance
                break
            tot_dist[k] = new_distance
            q.append(k)
    return ret_val


def vertices(_x, _y, grid):
    height = grid[_y][_x]
    ret_val = dict()
    for i_x in [_x + i for i in range(-1, 2, 1)]:
        for i_y in [_y + i for i in range(-1, 2, 1)]:
            if i_x == _x and i_y == _y:
                continue
            if abs(i_x - _x) > 0 and abs(i_y - _y) > 0:
                continue
            if i_y < 0 or i_y >= len(grid):
                continue
            if i_x < 0 or i_x >= len(grid[i_y]):
                continue
            neighbour_height = grid[i_y][i_x]
            if neighbour_height - height > 1:
                continue
            ret_val[(i_x, i_y)] = 1
    return ret_val


f = open('../data/ex12.txt')
lines = f.readlines()
graph = dict()
start = (0, 0)
end = (0, 0)
numeric_grid = []
starts = []
x = 0
y = 0
for line in [line.replace('\n', '') for line in lines]:
    new_line = []
    for c in line:
        if c == 'S':
            start = (x, y)
            starts.append((x, y))
        elif c == 'E':
            end = (x, y)
        elif c == 'a':
            starts.append((x, y))
        new_line.append(0 if c == 'S' else 25 if c == 'E' else (ord(c)-97))
        x += 1
    numeric_grid.append(new_line)
    y += 1
    x = 0

for y in range(0, len(numeric_grid)):
    for x in range(0, len(numeric_grid[y])):
        graph[(x, y)] = vertices(x, y, numeric_grid)

print(find_path(graph, start, end))
answers = []
for s in starts:
    path_length = find_path(graph, s, end)
    if path_length > 0:
        answers.append(path_length)
print(min(answers))
