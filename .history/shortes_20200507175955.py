def find_short(s):
    length = []
    for word in s.split():
        length.append(len(word))
    return sorted(length)[0]
def find_shorts(s):
    return min(len(x) for x in s.split())

 