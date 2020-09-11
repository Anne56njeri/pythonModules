def duplicate(nums):
    newDict = {}
    finalArr = []
    for i in nums:
        if i in newDict:
            newDict[i] +=1 
        else:
            newDict[i] = 1 
    print(newDict)        
    for i in newDict:
        print(newDict[i])
print(duplicate([4,3,2,7,8,2,3,1]))