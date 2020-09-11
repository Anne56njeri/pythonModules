# Don't overthinking a problem :)
# sorted returns an array 


def anagram(str):
        anagramGroup= {} 
        all = []
        for s in str:
            key = ''.join(sorted(s))
            # print(key)
            if key in anagramGroup:
                anagramGroup[key].append(s)
            else:
                anagramGroup[key]=[s]   
        print(anagramGroup)         
anagram(["eat", "tea", "tan", "ate", "nat", "bat"])  

