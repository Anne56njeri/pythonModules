def missing(A):
    # goal is to find the smallest int missing that is greater than 0
    # I would a range from 1 to max value in the arr 
    # o(n)
    # the number can't be a negative 
    if len(A) == 0:
        return 0 
    else:
        
        least = 100000 
        limit = 1000000
        counts = [0] * limit
        
        for i in range(len(A)):
            if arr[i]-1 >= 0:
                counts[arr[i]-1] += 1
                
        for i in range(len(counts)):
           if counts[i] == 0:
               if counts[i] < least:
                   return i+1
                   

print(missing([-1000000, 1000000]))           