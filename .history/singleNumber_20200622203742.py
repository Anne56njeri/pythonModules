def single(arr):
    # takes in an array of numbers 
    # and returns the non-repeated 
    # don't implement extra memory 
    arr = sorted(arr)
    i = 0 
    while i <len(sorted(arr))-1:
        if arr[i] != arr[i+1]:
            re(arr[i+1])

        i +=1
    
single([0,1,0,1,0,1,99])    