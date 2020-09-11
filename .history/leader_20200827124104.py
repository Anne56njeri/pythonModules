def leader(A):
    # A leader occurs more than n //2 times in the array 
    # meaning it makes up  more than half of the array 
    n = len(A)
    size = 0 
    for i in range(len(A)):
        if size == 0:
            size +=1 
            value = A[i]
        else:
            if value !=A[i]:
                size -=1 
            else:
                size +=1 
        print('size',size) 
        print('value') 
    candidate = -1    
    if size > 0:
        candidate = value
                  


leader([4,6,6,6,6,8,8])    