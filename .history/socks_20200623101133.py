def socks(arr):
    # sort the array 
    # keep count of available pairs
    # incerement i by 2 as a pair is made by 2 socks 
    
    count = 0 
    arr = sorted(arr)
    i = 1 
    print(arr)
    while i <len(arr)-1:
        if arr[i] == arr[i-1]:
            count +=1

               
        i +=2
    print(count)    
socks([1,2,1,2,1,3,2])        