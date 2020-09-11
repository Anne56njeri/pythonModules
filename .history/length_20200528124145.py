def removeDuplicates(nums):

    length = len(nums)
    i = 0
    for i in range(length):
        if nums[i] == nums[i+1]:
            print(nums[i])
        print(nums[i])    
removeDuplicates([1,1,1,2,2])          
