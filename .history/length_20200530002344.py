def removeDuplicates(nums):

    i = 0
   
    while  i < len(nums):
        print('index of i',i,'i---------->')

        j = i+1
        while j< len(nums):
          print('index of j',j,'j---->')
          if nums[i] == nums[j]:
            #   print(nums[i],'----was removed')
              nums.remove(nums[j])
          
          j +=1 
        i +=1     
    print(nums)
            
                

           
removeDuplicates([1,2,2,2])          
