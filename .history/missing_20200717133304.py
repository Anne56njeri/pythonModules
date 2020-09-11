def missing(arr):
    # sort the elements first 
    # what do you know about sequence 
    # that the next element is greater by one value 
    # once that doesn't happen just increment that value by one 
    # complexity of o(n)
    
    if len(arr) == 1:
        return arr[0]

    if arr != []:
        newArr = range(1,len(arr)+1)
        newSet = set(arr)

        print('set',newSet)
        print('arr',arr)
        i = 0 
        number = None
        while i < newArr:
            
            if arr[i]  in new:
                print(arr[i])
            else:
                number = arr[i]
                print('n',number)    
            i +=1

               
    else:
        return 1            
        
print(missing([2,3,1,5]))  