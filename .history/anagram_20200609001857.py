# Don't overthinking a problem :)


def anagram(str):
        anagramGroup= {} 
        for s in str:
            key = sorted(s)
            if key in anagramGroup:
                anagramGroup[key].append(s)
            else:
                anagramGroup    