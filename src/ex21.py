def calc(monk):
    global monkeys
    if type(monkeys[monk]) == int or type(monkeys[monk]) == float:
        ret_val = monkeys[monk]
    else:
        operation = monkeys[monk][1]
        m1 = monkeys[monk][0]
        m2 = monkeys[monk][2]

        if operation == '+':
            ret_val = calc(m1) + calc(m2)
        elif operation == '-':
            ret_val = calc(m1) - calc(m2)
        elif operation == '*':
            ret_val = calc(m1) * calc(m2)
        elif operation == '/':
            ret_val = calc(m1) / calc(m2)

    monkeys[monk] = ret_val
    return ret_val


lines = open('../data/ex21.txt')
monkeys = dict()
for line in lines:
    monkey = line[0:4]
    if line[6].isnumeric():
        monkeys[monkey] = int(line[6:])
    else:
        monkey1 = line[6:10]
        op = line [11]
        monkey2 = line[13:17]
        monkeys[monkey] = [monkey1,op,monkey2]

# root: qntq + qgth

print(monkeys)
monkeys['humn'] = 3555039910000 + 17543229
# while True:
#     a = calc('qntq')
#     if a > 8226036122233.0:
#         monkeys['humn'] += 10000000
#     else:
#         break
print(calc('qntq'))
print(calc('qgth'))
