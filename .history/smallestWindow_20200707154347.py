def min(s,t):
    no_of_chars = 256
    # first check if the length of the string is less than the string of the given pattern
    if len(t)> len(s):
        return ""
    else:
        # store the occurrences of the characters of the given pat in a hash pat
        hash_pat = [0] * no_of_chars
        hash_str = [0] * no_of_chars
        
        for i in range(len(t)):
            hash_pat[ord(t[i])] +=1
        print(hash_pat)

        for j in range(len(s)):
            hash_str[ord(t)]


     


min("ADOBECODEBANC","ABC")            