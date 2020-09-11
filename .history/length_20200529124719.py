def removeDuplicates(nums):

    i = 0
   
    while  i < len(nums):
        print('i---------->',i)

        j = i+1
        while j< len(nums):
          print('j---->',j)
          if nums[i] == nums[j]:
              del nums[i] 
              
              
          j +=1  


        # print(nums[i])  
       
         
        i +=1     
    print(nums)
            
                

           
removeDuplicates([1,1,2,2,2])          
