# Quick sort 
items = [6,20,8,19,56,23,87,41,49,53]
def quickSort(items,first,last):
    # calculate the split point 
    pivotIdx = partition(items,first,last)
    # now sort the two partitions 
    quickSort(items,first,pivotIdx-1)
    quickSort(items,pivotIdx-1,last)
    

