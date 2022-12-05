from copy import deepcopy as dc
f = open('../data/ex5.txt')
lines = f.readlines()
crates = [['B', 'Q', 'C'], ['R', 'Q', 'W', 'Z'], ['B', 'M', 'R', 'R', 'V'], ['C', 'Z', 'H', 'V', 'T', 'W'],
          ['D', 'Z', 'H', 'B', 'N', 'V', 'G'], ['H', 'N', 'P', 'C', 'J', 'F', 'V', 'Q'],
          ['D', 'G', 'T', 'R', 'W', 'Z', 'S'], ['C', 'G', 'M', 'N', 'B', 'W', 'Z', 'P'],
          ['N', 'J', 'B', 'M', 'W', 'Q', 'F', 'P']]
crates1 = dc(crates)
crates2 = dc(crates)
for line in lines:
    if line[0] != 'm':
        continue
    splt1 = line.split('from')
    n = int(splt1[0].replace('move', '').replace(' ', ''))
    splt2 = splt1[1].split(' to ')
    c1 = int(splt2[0])-1
    c2 = int(splt2[1])-1
    for i in range(0,n):
        dum = crates1[c1].pop()
        crates1[c2].append(dum)
    dum = crates2[c1][-1*n:]
    if len(crates2[c1]) > 0:
        del crates2[c1][-1*n:]
    crates2[c2] += dum

s1 = ''
for i in crates1:
    s1 += str(i[-1])
s2 = ''
for i in crates2:
    s2 += str(i[-1])

print(s1)
print(s2)





