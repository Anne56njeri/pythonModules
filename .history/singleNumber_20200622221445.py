def single(arr):
    # takes in an array of numbers 
    # and returns the non-repeated 
    # don't implement extra memory 
    # check for boundary cases 
    # the last element and final element
    if len(nums) == 1:
        return nums[0]
    numbers = {}
    for i in nums:
        if i in numbers:
            nums[1] +=1
        else:
            nums[1] = 1 
    # arr = sorted(arr)
    # if  arr[1] != arr[0]:
    #     return arr[0]
    # elif arr[len(arr)-1] != arr[len(arr)-2]:
    #     return arr[len(arr)-1]
    # else:
    #     i = 1
    #     while i < len(arr):
    #         if arr[i] != arr[i-1]:
    #             return arr[i-1]
    #         else:
    #             i = i+3  
             


        
print(single([0,1,1,1,2,2,2]))   