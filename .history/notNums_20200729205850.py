def nums(nums):
    if len(nums) == 0:
        return []
    else:
        n = len(nums)
        newArr = []
        newNums = range(1,n)
        newSet = set(nums)

        # for i in newNums:
        #     if i not in newSet:
        #         newArr.append(i)
        # return newArr
        nums.sort()
        nums = set(nums)
        for i in range(len(nums)):
            print(nums[i])



nums([4,3,2,7,8,2,3,1])    