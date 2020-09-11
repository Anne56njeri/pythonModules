def find_short(s):
    length = []
    for word in s.split():
        length.append(len(word))
    return sorted(length)[0]


find_short("geek for geeks")   