def print_error(s):
    alphabet = sorted(s)
    total = len(alphabet)
    if alphabet[-1] == 'm':
        print(0,"/",total)
    else:
        # error = total - alphabet.index('m')-1
        print(alphabet.index('a'))
        print(alphabet)
        # print(error,"/",total)


print_error('aaabbbbhaijjjzymmmm')