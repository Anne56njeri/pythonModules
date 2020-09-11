def removeDuplicates(nums):

    i = 0
   
    while  i =< len(nums)-1:
        print(nums[i])  
        if nums[i] == nums[i+1]:
            nums.remove(nums[i])
        else:
            nums.append(nums[i])  
        i +=1     
           
    # for i in range(length):
    #     print('i--------->',i)
    #     for j in range(i+1,length):
    #         print('j----->',j)
            
                

           
removeDuplicates([1,1,2])          
