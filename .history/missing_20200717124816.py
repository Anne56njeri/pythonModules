def missing(arr):
    # sort the elements first 
    # what do you know about sequence 
    # that the next element is greater by one value 
    # once that doesn't happen just increment that value by one 
    # complexity of o(n)
    arr = sorted(arr)
    i = 0 
    while i < len(arr):
        if arr[i] + 1 == arr[i+1]:
            i+=1
        else:
            return arr[i] +1    
        

print(missing())   