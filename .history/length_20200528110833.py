def removeDuplicates(nums):
    for i, n in enumerate(nums[:-1]):
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
        print(nums)  
removeDuplicates([1,1,2])          
