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
    
    for k in range(len(arr)-1,-1,-1):
        position = counts[arr[k]]- 1
        outputs[position] = arr[k]
        counts[arr[k]] -=1 
        
           

    print('out',outputs)    
def countin(A,m):
    n = len(A)
count = [0] * (m + 1)
4 for k in xrange(n):
5 count[A[k]] += 1
6 return count

def swap(A,B):
    n = len(A)
    sum_a = sum(A)
    sum_b = sum(B)
    m = max(A)+1
    d = sum_a - sum_b
    print(d)
    if d % 2 == 1:
        return False 
    count = countin(A,m)    
 
# 22 
# 24
swap([1,4,1,2,7,5,4],[2,4,5,6,2,3])        