# Quick sort 
items = [6,20,8,19,56,23,87,41,49,53]
def quickSort(items,first,last):
    if first< last:
        # calculate the split point 
        pivotIdx = partition(items,first,last)
        # now sort the two partitions 
        quickSort(items,first,pivotIdx-1)
        quickSort(items,pivotIdx-1,last)
def partition(dataValues,first,last):
    # choose the first item as the pivot value 
    pivotValue = dataValues[first]
    # establist the upper and lower indexes 
    lower = first + 1
    upper = last 

    # start searching for the crossing point 
    done = False 
    while not done:
        # advance the lower index
        while lower <= upper and dataValues[lower]
        # advance the upper index
        pass 
    temp = dataValues[first]
    dataValues[first] = dataValues[upper]





