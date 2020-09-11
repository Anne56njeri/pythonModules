def goalLatin(S):
    vowels = {'a','e','i','o','u'}
    S = S.split(" ")
    count = 1
    for i in range(len(S)):
        begin = 'a'
        if S[i][0] not in vowels:
            