f = open('../data/ex6.txt')
text = f.read().replace('\n', '')


def scan(length):
    for i in range(length, len(text)):
        sub = text[i - length:i]
        if len(sub) == len(set(sub)):
            print(sub + ' at: ' + str(i))
            break


scan(4)
scan(14)
