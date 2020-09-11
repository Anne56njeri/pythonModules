from itertools import permutations 

def anagram(str):
    angramTotal = []
    for i in range(len(str)):
        newWord = str[i]
        letter = [''.join(newWord) for newWord in permutations(str[0])]
        print