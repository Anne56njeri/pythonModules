'''
Given a text txt[0..n-1] and a pattern pat[0..m-1], 
write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.
'''
def pattern(txt,pat):
    if pat in txt:
        print('index',txt.index(pat))


pattern("AABAACAADAABAABA","AABA")    