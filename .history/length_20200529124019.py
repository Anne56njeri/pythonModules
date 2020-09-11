def removeDuplicates(nums):

    i = 0
   
    while  i < len(nums):
        print('i---------->',i)

        i +=1
        j = i+1
        while j< len(nums):
          j +=1  
          print('j---->',j)

        # print(nums[i])  
       
         
        i +=1     
    print(nums)
            
                

           
removeDuplicates([1,1,2,2,2])          
