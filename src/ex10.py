f = open('../data/ex10.txt')
lines = f.readlines()

cycle = 1
register = 1
score = 0
score_cycles = [20, 60, 100, 140, 180, 220]
sprite = [0, 1, 2]
CRT = ''

for line in lines:
    line = line.replace('\n', '')
    old_cycle = cycle
    old_register = register
    if 'noop' in line:
        cycle += 1
    else:
        cycle += 2
        register += int(line.split(' ')[1])
    for i in range(old_cycle, cycle):
        if i in score_cycles:
            score += (i*old_register)
            break
    for i in range(old_cycle, cycle):
        if ((i-1) % 40) in sprite:
            CRT += '#'
        else:
            CRT += '.'
    sprite = [register+i for i in[-1, 0, 1]]

print(score)
for i in range(0, len(CRT), 40):
    print(CRT[i:i+40])
