def duplicate(nums,k,t):
    m = None
    n = None

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if abs(nums[i] - nums[j]) == t:
                m = i 
                n = j 
    print(m,n)            
    if m is None or n is None:
        return False           
    
    if abs(nums[m] - nums[n] )== k:
        return True 
    return False        
print(duplicate([1,0,1,1],1,3))               
                


