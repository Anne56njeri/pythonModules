def duplicate(nums,k,t):
    m = None
    n = None

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if abs(nums[i] - nums[j]) <= t and j :
                m = i 
                n = j 
          
print(duplicate([1,0,1,1],1,2))               
                


