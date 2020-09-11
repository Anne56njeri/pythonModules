def socks(arr):
    # sort the array 
    # keep count of available pairs
    newArr = []
    count = 0 
    arr = sorted(arr)
    i = 0 
    while i <len(arr):
        if arr[i] == arr[i+1]:
            count +=1
        else:
            newArr.append(count)
            count = 0    
        i +=1