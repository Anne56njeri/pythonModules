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
        return arr[len(arr)-1]
    else:
        i = 1
        while i < len(arr):
            if arr[i] != arr[i-1]:
                return arr[i-1]
            else:
                i = i+3  
             


        
print(single([,2,2,2]))   