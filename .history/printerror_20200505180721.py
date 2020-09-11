def print_error(s):
    alphabet = sorted(s)
    total = len(alphabet)
    if alphabet[-1] == 'm':
        print(0,"/",total)
    else:
        alphabet = ''.join(alphabet)
        error = total - jio.rfind('m') -1
        output = f'{error}/{total}'
        print(str(output))



from re import sub
def printer_error(s):
    print "{}/{}".format(len(sub("[a-m]",'',s)),len(s))
printer_error('aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz')
