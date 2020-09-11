def nums(nums):
    if len(nums) == 0:
        return []
    else:
        n = len(nums)
        newArr = []
        newNums = range(1,n)
        newSet = set(nums)

        for i in newNums:
            if i not in newSet:
                newArr.append(i)
        return newArr
       



print(nums([1,1]))   