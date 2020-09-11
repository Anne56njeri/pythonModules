def removeDuplicates(nums):

    
   
    for n in nums:
        
        if n in nums:
            nums.remove(n)
        else:
            nums.add(n)  
    print(nums)        
           
    # for i in range(length):
    #     print('i--------->',i)
    #     for j in range(i+1,length):
    #         print('j----->',j)
            
                

           
removeDuplicates([1,1,2,2])          
