def moveZeroes(nums):
    # one thing maintain the position of all the non-zeroes 
    # loop through the array 
    #  get the last index of the array
    # if a digit is a zero then move it to the end 
    # else don't do anything
    lastIndex = len(nums) -1 
    for i in range(len(nums)):
        if nums[i] == 0:
            nums[lastIndex] = 0 
        else:
            nums[i] == nums[i]
    print(nums)    

moveZeroes([0,1,0,3])            
