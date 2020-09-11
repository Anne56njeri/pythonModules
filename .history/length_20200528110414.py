def removeDuplicates(nums):
    for i in range(len(nums)):
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
    print(nums)  
removeDuplicates([1,1,2])          
