def removeDuplicates(nums):

    length = len(nums)
    i = 0
    while i < length:
        print(nums[i]) 
        if(nums[i] == nums[i+1]){
            nums.remove()
        }
        
        i +=1
removeDuplicates([1,1,2])          
