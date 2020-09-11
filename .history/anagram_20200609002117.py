# Don't overthinking a problem :)


def anagram(str):
        anagramGroup= {} 
        for s in str:
            key = sorted(s)
            if key in anagramGroup:
                anagramGroup[key].append(s)
            else:
                anagramGroup[key] = s    
        print(an)         
anagram(["eat", "tea", "tan", "ate", "nat", "bat"])  

