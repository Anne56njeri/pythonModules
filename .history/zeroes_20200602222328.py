def moveZeroes(nums):
    # one thing maintain the position of all the non-zeroes 
    # loop through the array 
    #  get the last index of the array
    # if a digit is a zero then move it to the end 
    # else don't do anything
  
    zeroes = []
    i = 0
    while(i < len(nums)-1):
       
        if(nums[i] == 0):
            zeroes.append(nums[i])
            del nums[i]
            nums.ex
        else:    
          i +=1
    print(nums)        

   
            
    

moveZeroes([0,1,0,3,12])            
