from itertools import permutations 

def anagram(str):
    angramTotal = []
    for s in len(str):
        newWord = s
        print[''.join(newWord) for newWord in permutations()]