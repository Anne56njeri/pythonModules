def counting(arr):
    # keep count of the occurrences
    counts = [0 for i in range(100)]
    # final array 
    outputs = [0 for i in range(100)]
    for i in range(len(arr)):
        counts[ord(i)] +=1



counting([1,4,1,2,7,5,2])        