text = open('../data/ex1.txt', 'r').read()
elfs = sorted([sum(cs) for cs in [[int(x) for x in i] for i in [t.split() for t in text.split('\n\n')]]])
print(max(elfs))
print(sum(elfs[-3:]))
