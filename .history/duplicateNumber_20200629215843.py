def duplicate(arr):
    numbers = set()
    for i in range(len(arr)):
        if arr[i] not in numbers:
            numbers.add(arr[i])  
            arr.remove( arr[i] 
    print(arr)         

duplicate([1,3,4,2,2])    