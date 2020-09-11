def find_short(s):
    length = []
    for word in s.split():
        length.append(len(word))
    print(sorted(length))


find_short("geek for geeks")   