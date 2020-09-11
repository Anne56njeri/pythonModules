
# A[3,1,2,4,3]
# A[0] 3 - SUM(A[1,2,4,3])
'''
3 - SUM (10) = 7 
sum([3,1]) - sum(2,4,3)
4 - 9  = 5 
[3,1,2] - [4,3]
6 - 7 = 1 
[3,1,2,4] - [3]
10 - 3 = 7 
differences = [7,5,1,7]
  = 1
'''
def tape(A):
    
    if A != []:
        i = 0 
        
        min_diff = abs(A[0] - sum(A[1:])) # 7

        sumOfLeft = A[0]
        sumOfRight = sum(A[1:])

        for i in  range(1,len(A)-1):
            total = sumOfRight - sumOfLeft
            if abs(total) < min_diff:
                min_diff = abs(total)
            sumOfLeft +=A[i]
            sumOfRight   
            
           
        return min_diff    
        
    else:
        return 1     

print(tape([]))
def sumSlice(arr):
    results = 0 
    for  i in arr:
        results +=i
    return results    
