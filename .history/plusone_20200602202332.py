def plusOne(nums):
    end = len(nums) -1
    nums[end] = nums[:-1] +1
    print(nums)



plusOne([1,2,3])    