from itertools import permutations

def Time(A):
    # getting the different permutations 
    # get the one that falls between 0000 and 2359 
    # then place the semi colon in the proper place 
    # otherwise return an empty string 
    A = [str(i) for i in A]
    perm = permutations(A)
    time = ""

    newArray = []
    arr = []
    for i in list(perm):
        string = "".join(i)
        newArray.append(string)
      
    newArray = [int(i) for i in newArray]
   
    for i in newArray:
        if i >= 0000 and i <= 2359:
            arr.append(i)
    if arr !=[]:      
        newTime = arr[len(arr)-1]
        
        newTime = str(newTime)
        
        newTime = newTime.zfill(4)
        print(newTime)
        
        
    else:
        return ""    
    
    time = newTime[:2] + ":" + newTime[2:] 
    return time
          

        
        
print(Time([0,0,0,0]))       
