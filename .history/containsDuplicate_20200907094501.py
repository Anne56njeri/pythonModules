def duplicate(nums,k,t):
    m = None
    n = None

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if abs(nums[i] - nums[j]) == t:
                m = i 
                n = j 
               
    if m is not None and n is not None:
        if abs(nums[m] - nums[n] )== k:
            return True 
    return False        
print(duplicate([1,5,9,1,5,9],2,3))               
                


