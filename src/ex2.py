lines = open('../data/ex2.txt', 'r').readlines()
score_dict = dict()
score_dict['A X'] = 1 + 3
score_dict['A Y'] = 2 + 6
score_dict['A Z'] = 3 + 0
score_dict['B X'] = 1 + 0
score_dict['B Y'] = 2 + 3
score_dict['B Z'] = 3 + 6
score_dict['C X'] = 1 + 6
score_dict['C Y'] = 2 + 0
score_dict['C Z'] = 3 + 3

score = 0
for line in lines:
    score += score_dict[line.replace('\n', '')]

print(score)

score_dict['A X'] = 3 + 0
score_dict['A Y'] = 1 + 3
score_dict['A Z'] = 2 + 6
score_dict['B X'] = 1 + 0
score_dict['B Y'] = 2 + 3
score_dict['B Z'] = 3 + 6
score_dict['C X'] = 2 + 0
score_dict['C Y'] = 3 + 3
score_dict['C Z'] = 1 + 6

score = 0
for line in lines:
    score += score_dict[line.replace('\n', '')]

print(score)
