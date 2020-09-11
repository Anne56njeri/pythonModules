from itertools import permutations 

def anagram(str):
    angramTotal = []
    for i in range(len(str)):
        newWord = str[i]
        print[''.join(newWord) for newWord in permutations(str[0])]