f = open('../data/ex9.txt')
lines = f.readlines()
Ts = {(0, 0)}

H = (0, 0)
T = (0, 0)


def new_tail(t, h, direction):
    if abs(t[0]-h[0]) > 1 or abs(t[1]-h[1]) > 1:
        if direction == 'U':
            t = (h[0], h[1]-1)
        if direction == 'D':
            t = (h[0], h[1]+1)
        if direction == 'L':
            t = (h[0]+1, h[1])
        if direction == 'R':
            t = (h[0]-1, h[1])
    return t


for line in lines:
    d = line.split(' ')[0]
    for i in range(0, int(line.split(' ')[1])):
        if d == 'U':
            H = (H[0], H[1]+1)
        if d == 'D':
            H = (H[0], H[1]-1)
        if d == 'L':
            H = (H[0]-1, H[1])
        if d == 'R':
            H = (H[0]+1, H[1])
        T = new_tail(T, H, d)
        Ts.add(T)

print(Ts)
print(len(Ts))
