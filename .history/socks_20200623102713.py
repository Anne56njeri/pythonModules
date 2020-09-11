def socks(arr,n):
    # sort the array 
    # keep count of available pairs
    # incerement i by 2 as a pair is made by 2 socks 
    
    count = 0 
    arr = sorted(arr)
    i = 1 
    print(arr)
    while i <n:
        if arr[i] == arr[i-1]:
            count +=1
        print('count',count)

        print('i',i)    

               
        i +=2
    print(count)    
socks([4,5,5,5,6,6,4,1,4,4,3,6,6,3, 6 ,1, 4, 5, 5, 5],20)        