def longest(s1,s2):
    b= s1+s2
    c = ''.join(sorted(set(b)))
    print(c)

longest('aretheyhere','yestheyarehere')