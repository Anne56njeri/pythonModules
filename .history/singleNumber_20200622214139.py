def single(arr):
    # takes in an array of numbers 
    # and returns the non-repeated 
    # don't implement extra memory 
    # check for boundary cases 
    # the last element and final element 
    arr = sorted(arr)
    if  arr[1] != arr[0]:
        return arr[0]
    elif arr[len(arr)-1] != arr[len(arr)-2]:
        return arr   


    print(arr)        
print(single([0,1,0,1,0,1,99]))   