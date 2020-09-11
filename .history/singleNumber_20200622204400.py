def single(arr):
    # takes in an array of numbers 
    # and returns the non-repeated 
    # don't implement extra memory 
    arr = sorted(arr)
    i = 0 
    while i < len(arr)-1:
        if arr[i] == arr[i+1]:
            del arr[i]
    print(arr)        
print(single([0,1,0,1,0,1,99]))   