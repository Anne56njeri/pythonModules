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
    for i in newItem:
        if newItem[i] >=2         

mean([4,4,4,6,2])    