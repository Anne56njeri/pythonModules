def twoSum(nums,target):
    # loop through the array 
    # add the two nums checking whethere they are equal to the target 
    # when you get one that is equal to the target append the indices...
    index = []
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            
            if nums[i]+ nums[j] == target:
                index.append(nums[i])
                index.append(nums[j])
    print(index)
def  two(nums,S):
    sums = []
    check = {}
    for i in range(len(nums)):
        minus = S - nums[i]
        if str(minus)  in check:
            sums.append(nums[i],minus)



twoSum([2, 7, 11, 15],9)        