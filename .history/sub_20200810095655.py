# 

def subs(str1,str2):
    m = len(str1)
    n = len(str2)
    i = 0
    j = 0 
    # in the case where str1[j] == str[i] move to the next letter in j  and also i 
    # but if not equal stay on the same letter then you only increment j if str[j] == str[i]
    while j< m and i < n:
        if str1[j] == str2[i]:
            j +=1
            print("j--->",j)  

        i +=1 
        
    if j == m:
        print("true") 
    else:
        print("false")



   

subs("gksrek","geeksforgeeks")
     
# subs("leeeeetcode",
# "")        
        
