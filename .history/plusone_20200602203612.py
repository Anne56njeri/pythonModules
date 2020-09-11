def plusOne(nums):
    end = len(nums) -1
    nums[end] = nums[end] +1 
    if nums[end] >= 10:
        for i in str(nums[end]):
            nums[end] = int(i)


    
    print(nums)



plusOne([9])    