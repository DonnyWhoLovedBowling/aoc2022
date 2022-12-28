def snafu_to_dec(_snafu):
    num = 0
    for i, c in enumerate(_snafu[::-1]):
        base = 5**i
        if c == '2':
            num += 2 * base
        elif c == '1':
            num += 1 * base
        elif c == '1':
            num += 1 * base
        elif c == '-':
            num -= 1 * base
        elif c == '=':
            num -= 2 * base
    return num


def dec_to_snafu(_dec):
    _snafu = ''
    while True:
        dum = _dec // 5
        rem = _dec % 5
        if rem == 4:
            c = '-'
            dum += 1
        elif rem == 3:
            c = '='
            dum += 1
        else:
            c = str(rem)
        _snafu = c + _snafu
        if dum == 0:
            break
        _dec = dum
    return _snafu


score = 0
lines = open('../data/ex25.txt')
for line in lines:
    snafu = line.replace('\n', '').strip()
    dec = snafu_to_dec(snafu)
    print(snafu, dec)
    score += dec

print(score)
print(dec_to_snafu(score))
