def colors(nums):
    # sort the numbers 
    # using bubble sort
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] > nums[j]:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
    print(nums)            
    return nums
    
                
