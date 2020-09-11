def h(arr):
    n = len(arr)
    i = n-1
    while i >=0:
        print(arr[i],n-i,i)
        if arr[i]< n-i:
            break
        i -=1
    return n-i-1   
     
print(h([3,0,6,1,5]))