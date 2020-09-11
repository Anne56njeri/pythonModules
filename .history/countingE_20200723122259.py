def counting(arr):
    # keep count of the occurrences
    m = max(arr)+1
    counts = [0 for i in range(m)]
    
    outputs = [0 for i in range(m)]
    # we keep the record of the occurences of the various numbers
    for i in range(len(arr)):
        counts[arr[i]] +=1
    # now to get the running sum
    total = 0
    for i in range(len(counts)):
        total += counts[i]
        counts[i] = total
    # next step is to now map the numbers to there proper positions starting from the end of the arr
    for k in range(len(arr)-1,0,-1):
        position = counts[arr[k]] - 1
        outputs[position] = arr[k]
        print(counts[arr[k]]) 
           

    print(counts)    



counting([1,4,1,2,7,5,2])        