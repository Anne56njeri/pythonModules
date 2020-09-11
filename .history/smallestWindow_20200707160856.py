def min(s,t):
    no_of_chars = 256
    count = 0 
    start = 0 
    start_index = -1
    min_len = float('inf')

    print(start,start_index,min_len)
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
            if hash_pat[ord(t[j])] <= hash_str[ord(s[j])] and hash_pat[ord(t[j]) !=0]:
                count +=1
            # when the count gets to the length of the pattern string then the window string contains the pattern 
                
            if count == len(t):
                 # here we'll try minimize the window --> how 
                 # if the window contains repeating characters that are not in the pattern 
                 # we ignore them 
                 # also if a character is there and not available in the pattern please ignore it 
                while(hash_str[ord(s[start])] > hash_pat[ord(string[start])] or :





     
# first substring ADOBEC
'''
in the while loop we are checking for ----> value of A which is one is greater than  value of A in the pattern 
the pattern('ABC') this is checking to remove any repeated strings  cause value of A is hash_str[65] == 2

the other condition we aim to remove any useless characters 

'''

min("ADOBECODEBANC","ABC")            