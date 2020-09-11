def min(s,t):
    no_of_chars = 256
    count = 0 
    # first check if the length of the string is less than the string of the given pattern
    if len(t)> len(s):
        return ""
    else:
        # store the occurrences of the characters of the given pat in a hash pat
        hash_pat = [0] * no_of_chars
        hash_str = [0] * no_of_chars
        # here we create a array where we store the number of occurences of a char based on its ascii value 
        for i in range(len(t)):
            hash_pat[ord(t[i])] +=1
        print(hash_pat)

        for j in range(len(s)):

            hash_str[ord(t[j])] +=1
            if hash_pat[ord(j)]


     


min("ADOBECODEBANC","ABC")            