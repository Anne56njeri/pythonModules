def removeDuplicates(nums):

    i = 0
   
    while  i < len(nums)-1:
        # print(nums[i])  
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
         
        i +=1     
    print(nums)
            
                

           
removeDuplicates([1,1,2,2,2])          
