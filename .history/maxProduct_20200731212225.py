import sys 
# time complexity is o(n3 ) and space is o(1)
def maxThree(arr):
    if len(arr) < 3:
        return -1 
    maxProduct = -(sys.maxsize -1)
    print(maxProduct) 
    n = len(arr)
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range(j+1,n):
                print('i',arr[i],'j',arr[j],'k',arr[k])
                product = arr[i] * arr[j] * arr[k]
                if product > maxProduct:
                    maxProduct = product 
    return maxProduct                

# Optimal solution 
def maxOp(arr):
    arr.sort()
    first = arr[n-1] * arr[n-2] * arr[n-3] 
    second = arr[0]        
print(maxThree([-3,1,2,-2,5,6]))    