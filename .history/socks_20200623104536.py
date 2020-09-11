def socks(arr,n):
    # sort the array 
    # keep count of available pairs
    # incerement i by 2 as a pair is made by 2 socks 
    
    count = 0 
    arr = sorted(arr)
    i = 1 
    print(arr)
    # while i <n:
    #     print('i',i)
    #     print(arr[i],'---->',arr[i-1])
    #     if arr[i] == arr[i-1]:
    #         count +=1
    #     print('count',count)

            

               
    #     i +=2
    # print(count)  
    newSet = {}
    pairs = 0
    for i in arr:
        if i not in newSet:
            newSet[i]
        else:
            pairs +=1
            newSet.remove(i)


socks([4,5,5,5,6,6,4,1,4,4,3,6,6,3,6,1,4,5,5,5],20)        