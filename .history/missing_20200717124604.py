def missing(arr):
    # sort the elements first 
    # what do you know about sequence 
    # that the next element is greater by one value 
    # once that doesn't happen just increment that value by one 
    # complexity of o(n)
    newrr = range(1,len(arr)+1)
    for i in newrr:
        print(i)

missing([2,3,1,5])    