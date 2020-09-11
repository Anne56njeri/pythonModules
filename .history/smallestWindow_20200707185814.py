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
        # print(hash_pat)

        for j in range(len(s)):

            hash_str[ord(s[j])] +=1
            if hash_str[ord(s[j])] <= hash_pat[ord(s[j])] and hash_pat[ord(s[j])] !=0:
                count +=1
            # when the count gets to the length of the pattern string then the window string contains the pattern 
               
            if count == len(t):
                 # here we'll try minimize the window --> how 
                 # if the window contains repeating characters that are not in the pattern 
                 # we ignore them 
                 # also if a character is there and not available in the pattern please ignore it 
                 # this while loop is for only valid substrings and we are trying to minimize the string 
                 # so we try minimizing the start   

                # once the window is found we try and minimize it 
                # incase you can't minimize it move the j pointer 

                while hash_str[ord(s[start])] > hash_pat[ord(s[start])] or hash_pat[ord(s[start])] == 0:
                    
                    if hash_str[ord(s[start])] > hash_pat[ord(s[start])]:
                        # we decrease the value
                        hash_str[ord(s[start])] -=1
                        
                    print("hereee")
                    # print('substring',s[start_index:start_index + min_len])     
                    start +=1 
                print('start',start) 

                print('j---->',j)    
                window_length = j - start +1 
                print('window length',window_length)  
                print('substring',s[start:j+1]) 
                if min_len > window_length:
                    min_len = window_length 
                    start_index = start 
                      







     
# first substring ADOBEC
'''
--- ADOBEC --> this is the first substring 

in the while loop we are checking for ----> value of A which is one is greater than  value of A in the pattern 
the pattern('ABC') this is checking to remove any repeated strings  cause value of A is hash_str[65] == 2

the other condition we aim to remove any useless characters where if the value of that char in the pattern hash is 0 

'''

min("ADOBECODEBANC","ABC")            