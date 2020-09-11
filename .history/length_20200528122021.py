def removeDuplicates(nums):

    length = len(nums)
    i = 0
    while i < length:
        print(nums[i]) 
        if(nums[i] == nums[i+1]):
            nums.remove(nums[i])
            length = length -1
        i +=1
    print(nums)    
removeDuplicates([11,1,2])          
