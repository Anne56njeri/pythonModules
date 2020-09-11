def topKFrequent(nums,k):
        newDict = {}
        newArr = []
        for i in nums:
            if i in newDict:
                newDict[i] +=1
            else:
                newDict[i] = 1
        print(newDict)        
        for i in newDict:
            if newDict[i] >= k:
                newArr.append(i)

        return newArr
print(topKFrequent([3,0,1,0],1))       