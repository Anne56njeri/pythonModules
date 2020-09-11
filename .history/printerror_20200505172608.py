def print_error(s):
    # numerator = 0
    alphabet = sorted(s)
    total = len(alphabet)
    if alphabet[-1] == 'm':
        print(0,"/",total)
    else:
        print(alphabet.index('m'))
        print(total)


print_error('aaabbbbhaijjjxxm')