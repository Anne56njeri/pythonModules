import itertools

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
    print(arr)        
    if arr !=[]:      
        newTime = arr[len(arr)-1]
        
        newTime = str(newTime)
        
        newTime = newTime.zfill(4)
        print(newTime)
        
        
    else:
        return ""    
    
    time = newTime[:2] + ":" + newTime[2:] 
    return time
          

def time(A):
    max_time = -1
    # enumerate all possibilities,with the permutation() fun 
    print(list(itertools.permutations(A)))
    for h,i,j,k in itertools.permutations(A):
        hour = h*10 + i 
        minute = j*10 + k
        if hour < 24 and minute < 60:
            max_time = max(max_time,hour * 60 + minute)
    if max_time == -1:
        return ""
    else:
        return "{:02d}:{:02d}".format(max_time // 60,max_time % 60)                
        
print(time([0,2,3,0]))       
