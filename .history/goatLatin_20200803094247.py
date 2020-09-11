def goalLatin(S):
    vowels = {'a','e','i','o','u'}
    S = S.split(" ")
    count = 1
    for i in range(len(S)):
        begin = 'a'
        newWord = ""
        if S[i][0] in vowels:
            begin = begin * count
            newWord += S[i] + "ma" + begin 
        else:
            begin = begin * count
            newWord = S[i][1:] + "ma" + begin

            

            