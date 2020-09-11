def plusOne(nums):
    end = len(nums) -1
    nums[end] = nums[end] +1 
    if nums[end] >= 10:
       newArr = [int(i) for i in str(nums[end])]

       nums.remove(nums[end])
       nums.extend(newArr)
    else:
        return nums   


    
    



plusOne([9])    