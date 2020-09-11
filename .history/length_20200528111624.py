def removeDuplicates(nums):
    for i in range(nums[:-1]):
        if n == nums[i+1]:
            nums.remove(nums[i])

    print(nums)  
removeDuplicates([1,1,2])          
