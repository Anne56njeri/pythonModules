def print_error(s):
    alphabet = sorted(s)
    total = len(alphabet)
    if alphabet[-1] == 'm':
        print(0,"/",total)
    else:
        jio = ''.join(alphabet)
        print(jio.rfind('m')-1)
        error = total - jio -1

        # print(alphabet)
        print(error,"/",total)


print_error('aaabbbbhaijjjzymmmm')