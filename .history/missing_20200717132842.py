def missing(arr):
    # sort the elements first 
    # what do you know about sequence 
    # that the next element is greater by one value 
    # once that doesn't happen just increment that value by one 
    # complexity of o(n)
    if len(arr) == 1:
        return arr[0]

    if arr != []:
        newArr = set(range(1,len(arr)+2))
        print('arr',newArr)
        i = 0 
        while i < len(arr):
            print(arr[i])
            if arr[i] not in newArr:
                print(arr[i])
            i +=1

               
    else:
        return 1            
        
print(missing([2,3,1,5]))  