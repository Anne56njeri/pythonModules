# Don't overthinking a problem :)


def anagram(str):
        anagramGroup= {} 
        for s in str:
            key = sorted(s)
            i