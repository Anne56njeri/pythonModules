def missing(arr):
    # sort the elements first 
    # what do you know about sequence 
    # that the next element is greater by one value 
    # once that doesn't happen just increment that value by one 
    # complexity of o(n)
    if len(arr) == 1:
        return arr[0]

    if arr != []:
        arr = sorted(arr)
        i = 0 
               
    else:
        return 1            
        
print(missing([2,3,1,5]))  