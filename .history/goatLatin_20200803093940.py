def goalLatin(S):
    vowels = {'a','e','i','o','u'}
    S = S.split(" ")
    count = 1
    for i in range(len(S)):
        begin = 'a'
        