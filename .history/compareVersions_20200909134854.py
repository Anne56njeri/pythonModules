# space complexity = o(n)--> two list 
# time complexity = o(n) --> loop runs for 
def compare(version1,version2):
    # split where there are ,
    # then loop through both of them 
    # if v1 > v2 return 1 
    # if v1 < v2 return -1
    # otherwise return 0 
    
    v1 = [int(i) for i in version1.split(".")]
    v2= [int(i) for i in version2.split(".")]
    # if len(v1) > len(v2):
    #     while len(v1) !=len(v2):
    #         v2.append(0)
        
        
    # else:
    #     while len(v1) !=len(v2):
    #         v1.append(0)
   
    for i in range(max(len(v1),len(v2))):
        vi = v1[i] if i < len(v1) else 0 
        vii = v2[i] if i < len(v2) else 0 
        if vi > vii:
            return 1 
        elif vi < vii:
            return -1
    return 0                  
   
print(compare("1.0.1","1"))                



