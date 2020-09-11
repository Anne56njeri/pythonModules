# sort them in increasing order 
# search through  the list 
# unsorted list 
# first item min value = first item 
# find a min value re assign 
# search for smallest item 
# move to first position 
# 
def selection(arr):
    for i in range(len(arr)):
        minValue = arr[i]
        for j in range(i+1,len(arr)):
            if arr[j] < minValue:
                minValue = arr[j] 
        temp = arr[i]        
        arr[i]


selection([5,2,8,14,1,16])    