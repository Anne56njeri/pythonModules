def missing(arr):
    # goal is to find the smallest int missing that is greater than 0
    # I would a range from 1 to max value in the arr 

        counts = [0] * limit
        
        for i in range(len(arr)):
            if arr[i]-1 >= 0:
                counts[arr[i]-1] += 1
        print(counts)        
        for i in range(len(counts)):
           if counts[i] == 0:
               if counts[i] < least:
                   return i+1
                   

print(missing([-1,-3,1]))           