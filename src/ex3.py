def char_to_int(c):
    if c.isupper():
        return (ord(c)-64)+26
    else:
        return ord(c)-96


f = open('../data/ex3.txt')
lines = f.readlines()
score = 0
for line in lines:
    line = line.replace('\n', '')
    br = int(len(line)/2)
    s1 = line[0:br]
    s2 = line[br:]
    score += char_to_int(list((set(s1) & set(s2)))[0])
print(score)
score = 0

for i in range(0, len(lines), 3):
    s1 = lines[i].replace('\n', '')
    s2 = lines[i+1].replace('\n', '')
    s3 = lines[i+2].replace('\n', '')
    score += char_to_int(list((set(s1) & set(s2) & set(s3)))[0])

print(score)
