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
        if newDict[i] == 2:
            finalArr.append(newDict[i])
    return finalArr
print(duplicate([4,3,2,7,8,2,3,1]))