def counting(arr):
    # keep count of the occurrences
    m = max(arr)+1
    counts = [0 for i in range(m)]
    
    outputs = [0 for i in range(9)]
    for i in range(len(arr)):
        counts[arr[i]] +=1
        

    print(counts)    



counting([1,4,1,2,7,5,2])        