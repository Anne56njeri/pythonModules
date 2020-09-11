def waveSort(arr):
    # we get the length of the array
    n = len(arr)
    # we sort the array
    arr.sort()
    print(arr)
    left = 0 
    # we loop from the middle of the array 
    right = n // 2
   
    
    while left < (n // 2) and right < n:
        print('left',arr[left])
        print('right',arr[right])
        if arr[right] > arr[left]:
            left +=1
            right +=1
        else:
            return 'false'
    return 'true'            


waveSort([0, 2, 4, 4, 4, 14, 22])    