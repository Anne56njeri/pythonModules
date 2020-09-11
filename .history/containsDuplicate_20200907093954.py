def duplicate(nums,k,t):
    m = None
    n = None

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] - nums[j] =< t:
                m = i 
                n = j 
    print(m,n)
                
                


