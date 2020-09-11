def socks(arr):
    # sort the array 
    # keep count of available pairs
    # incerement i by 2 as a pair is made by 2 socks 
    newArr = []
    count = 0 
    arr = sorted(arr)
    i = 0 
    print(arr)
    while i <len(arr)-1:
        if arr[i] == arr[i+1]:
            count +=1
        else:
               
        i +=2
    print(newArr)    
socks([10, 20 ,20 ,10 ,10, 30, 50, 10 ,20])        