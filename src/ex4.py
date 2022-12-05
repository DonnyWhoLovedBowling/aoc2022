f = open('../data/ex4.txt')
lines = f.readlines()

score1 = 0
score2 = 0
for line in lines:
    elfs = line.replace('\n', '').split(',')
    elf1 = elfs[0].split('-')
    elf1_set = set(range(int(elf1[0]), int(elf1[1]) + 1))
    elf2 = elfs[1].split('-')
    elf2_set = set(range(int(elf2[0]), int(elf2[1]) + 1))
    if len(elf1_set.union(elf2_set)) == max(len(elf1_set), len(elf2_set)):
        score1 += 1
    if len(elf1_set.intersection(elf2_set)) > 0:
        score2 += 1

print(score1)
print(score2)
