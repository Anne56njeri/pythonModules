'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], 
write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
'''
def pattern(txt,pat):
    # Catepillar algorithm
    # we have  a left and right pointer 
    # then the length of the search string 
    # when searching for the string when they don't match move the right pointer 
    # to increase the window size 
    # if the match return poisition of left, store it in an array 
    # when the len(sub) > substring move the left pointer 

    if pat in txt:

        print('index',txt.index(pat))


pattern("AABAACAADAABAABA","AABA")    