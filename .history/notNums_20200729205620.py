def nums(nums):
    if len(nums) == 0:
        return []
    else:
        n = len(nums)
        newArr = []
        newN = range(1,n)

        for i in nums:
            if i not in newSet:
                newArr.append(i)
        print(newArr)



nums([4,3,2,7,8,2,3,1])    