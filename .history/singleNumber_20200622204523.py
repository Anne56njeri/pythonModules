def single(arr):
    # takes in an array of numbers 
    # and returns the non-repeated 
    # don't implement extra memory 
    arr = sorted(arr)
    i = 0 
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            arr.remove(arr[i])
            del arr[i+1]   
        i +=1    
    print(arr)        
print(single([0,1,0,1,0,1,99]))   