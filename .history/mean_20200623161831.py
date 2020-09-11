import statistics

def mean(arr):
    # mean = sum(arr) / len(arr)
    # mode = max(arr,key=arr.count)
    # print(mean)
    # print(mode) 

    mean = sum(arr)/len(arr)
    newItem = {}
    for i in arr:
        if i in newItem:
            newItem[i]+=1
        else:
            newItem[i] = 1
    print(newItem)
    
    # the key whose value is the largest 
    maxValue = max (newItem,key = lambda k:newItem[k])
    print(maxValue)
    key = lambda
    if maxValue == mean:
        return 1 
    else:
        return 0        
    # for i in newItem:
    #     if newItem[i] >=2 and i == mean:
    #         return 1
    #     else:
    #         return 0            

print(mean([1,6,2]))   