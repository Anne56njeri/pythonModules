items = []
def mergeSort(data):
    if len(data) > 1:
        mid = len(data) // 2
        leftArr = data[:mid]
        rightArr= data[mid:] 
        # now to perform the merge 
        i = 0 
        j = 0 
        k = 0

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                data[k] =leftArr[i]
                i +=1 
            else:
                data[k] = rightArr[j]
                j +=1  
            k +=1 
        #  if the left array still has value, add them 
        # TODO: if the right array still has values add them 
        #          

