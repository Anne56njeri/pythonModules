def removeDuplicates(nums):

    if len(nums) == 0:
        return 0
    i = 0    
    for j in range(len(nums)):
        if nums[j] != nums[i]:
            i +=1
            nums[i] = nums[j]
    print(i)        
    print(i+1)         
            
                

           
removeDuplicates([1,1,2,2,2])          
