def duplicate(arr):
    numbers = set()
    for i in range(len(arr)):
        if arr[i] in numbers:
        else:
            numbers.add(arr[i])  
              

duplicate([1,3,4,2,2])    