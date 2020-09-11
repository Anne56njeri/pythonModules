def removeDuplicates(nums):

    
   
    for i in range(len(nums)):
        
        if nums[i] in nums:
            nums.remove(nums[i])
        else:
            nums.add(nums[i])  
           
    # for i in range(length):
    #     print('i--------->',i)
    #     for j in range(i+1,length):
    #         print('j----->',j)
            
                

           
removeDuplicates([1,1,1,2,2])          
