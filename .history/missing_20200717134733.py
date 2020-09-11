def missing(arr):
    # sort the elements first 
    # what do you know about sequence 
    # that the next element is greater by one value 
    # once that doesn't happen just increment that value by one 
    # complexity of o(n)
    
    # if len(arr) == 1:
    #     return arr[0]

    if arr != []:
        newArr = range(1,len(arr)+2)
        newSet = set(arr)
        i = 0 
        print(newArr)
        print(newSet)
        while i < len(newArr):
            if newArr[i] not in newSet:
                return newArr[i]

            i +=1

        return 1      
    else:
        return 1            
        
print(missing([1]))  