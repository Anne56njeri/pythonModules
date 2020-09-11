def waveSort(arr):
    # we get the length of the array
    n = len(arr)
    arr.sort()
    print(arr)
    left = 0 
    right = n // 2
    print(right)
    while left < (n // 2) and right < n:
        print('left',arr[left])
        print('right',arr[right])
        if arr[right] > arr[left]:
            left +=1
            right +=1
            


waveSort([0, 2, 4, 4, 4, 14, 22])    