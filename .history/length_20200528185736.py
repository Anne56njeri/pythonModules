def removeDuplicates(nums):

    length = len(nums)
    i = 0
    for i in range(length):
        if nums[i] in nums:
            nums.remove(nums[i])
        else:
            nums.add(nums[i])  
    pr          
    # for i in range(length):
    #     print('i--------->',i)
    #     for j in range(i+1,length):
    #         print('j----->',j)
            
                

           
removeDuplicates([1,1,1,2,2])          
