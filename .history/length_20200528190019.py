def removeDuplicates(nums):

    
   
    for n in nums:
        
        if n in nums:
            nums.remove(nums[i])
        else:
            nums.add(nums[i])  
    print(nums[i])        
           
    # for i in range(length):
    #     print('i--------->',i)
    #     for j in range(i+1,length):
    #         print('j----->',j)
            
                

           
removeDuplicates([1,1,1,2,2])          
