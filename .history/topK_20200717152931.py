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
topKFrequent([1,1,1,2,2,3],2)        