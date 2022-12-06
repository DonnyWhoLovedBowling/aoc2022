f = open('../data/ex6.txt')
text = f.read().replace('\n', '')

for i in range(4, len(text)):
    sub = text[i-4:i]
    if len(sub) == len(set(sub)):
        print(sub + ' at: ' + str(i))
        break

for i in range(14, len(text)):
    sub = text[i-14:i]
    if len(sub) == len(set(sub)):
        print(sub + ' at: ' + str(i))
        break
