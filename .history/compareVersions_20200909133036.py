def compare(version1,version2):
    # split where there are ,
    # then loop through both of them 
    # if v1 > v2 return 1 
    # if v1 < v2 return -1
    # otherwise return 0 
    v1 = version1.split(".")
    v2 = version2.split(".")
    
    v1 = [int(i) for i in v1]
    v2= [int(i) for i in v2]
    if len(v1) > len(v2):
        length = len(v1)
        
    else:
        length = len(v2) 
    for i in range(length)    

   /                  
   
print(compare("1","1.1"))                



