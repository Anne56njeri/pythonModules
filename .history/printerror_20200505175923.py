def print_error(s):
    alphabet = sorted(s)
    total = len(alphabet)
    if alphabet[-1] == 'm':
        print(0,"/",total)
    else:
        jio = ''.join(alphabet)
        print("last m",jio.rfind('m'))
        error = total - jio.rfind('m') -1
        print(alphabet)
        output = f'{error}/{total}'
        print(output)


print_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz')