def moveZeroes(nums):
    # one thing maintain the position of all the non-zeroes 
    # loop through the array 
    #  get the last index of the array
    # if a digit is a zero then move it to the end 
    # else don't do anything
    lastIndex = len(nums) -1 
    zeroes = []
    i = 0
    while(i < lastIndex):
        print(nums[i])
        # if(nums[i] == 0):
        #     # zeroes.append(nums[i])
        #     nums.remove(nums[i])
            i +=1
    print(nums)        

   
            
    

moveZeroes([0,1,0,3,12])            
