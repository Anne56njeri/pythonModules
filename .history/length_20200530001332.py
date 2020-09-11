def removeDuplicates(nums):

    i = 0
   
    while  i < len(nums):
        print(i,'i---------->','nums at i',nums[nums[i]])

        j = i+1
        while j< len(nums):
          print(j,'j---->','nums at j',nums[nums[j]])
          if nums[i] == nums[j]:
              print(nums[i],'----was removed')
              nums.remove(nums[i])
          else:
             j +=1 
        i +=1     
    print(nums)
            
                

           
removeDuplicates([1,2,2])          
