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
        # TODO: recursively break down the array 
        mergeSort(leftArr)
        mergeSort(rightArr)

        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                data[k] =leftArr[i]
                i +=1 
            else:
                data[k] = rightArr[j]
                j +=1  
            k +=1 
        #  if the left array still has value, add them 
        while i < len(leftArr):
            data[k] = leftArr[i]
            i +=1
            k +=1

        # TODO: if the right array still has values add them 
        while j < len(rightArr):
            data[k] = rightArr[j]
            j +=1
            k +=1   

