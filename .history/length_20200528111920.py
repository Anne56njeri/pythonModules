def removeDuplicates(nums):

    
    for i in range(length-1):
        
       if nums[i] == nums[i+1]:
           length = length - 1
           nums.remove(nums[i])
        

    print(nums)  
removeDuplicates([1,1,2])          
