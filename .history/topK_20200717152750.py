def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newDict = {}
        newArr = []
        for i in nums:
            if i in newDict:
                newDict[i] +=1
            else:
                newDict[i] = 1
                
        for i in newDict:
            if newDict[i] == k:
                newArr.append(i)
        return newArr
topKFrequent()        