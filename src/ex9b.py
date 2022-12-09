import math
f = open('../data/ex9.txt')
lines = f.readlines()
Ts = {(0, 0)}
H = [(0, 0)]*10


def must_move(t, h):
    return abs(t[0]-h[0]) > 1 or abs(t[1]-h[1]) > 1


def new_tail(t, h):
    x_dir = 0
    y_dir = 0
    if must_move(t, h):
        if math.dist(t, h) > 2: #diagonal
            if h[0] > t[0] and h[1] > t[1]:
                x_dir = 1
                y_dir = 1
            elif h[0] < t[0] and h[1] > t[1]:
                x_dir = -1
                y_dir = 1
            elif h[0] > t[0] and h[1] < t[1]:
                x_dir = 1
                y_dir = -1
            elif h[0] < t[0] and h[1] < t[1]:
                x_dir = -1
                y_dir = -1
        else:
            if h[0] > t[0]:
                x_dir = 1
            if h[0] < t[0]:
                x_dir = -1
            if h[1] > t[1]:
                y_dir = 1
            if h[1] < t[1]:
                y_dir = -1

    return t[0] + x_dir, t[1] + y_dir


for line in lines:
    d = line.split(' ')[0]
    for j in range(0, int(line.split(' ')[1])):
        if d == 'U':
            H[0] = (H[0][0], H[0][1]+1)
        if d == 'D':
            H[0] = (H[0][0], H[0][1]-1)
        if d == 'L':
            H[0] = (H[0][0]-1, H[0][1])
        if d == 'R':
            H[0] = (H[0][0]+1, H[0][1])
        for i in range(0, 9):

            T_new = new_tail(H[i + 1], H[i])
            H[i+1] = T_new
            if i == 8:
                Ts.add(H[9])
    print(H)
print(Ts)
print(len(Ts))



