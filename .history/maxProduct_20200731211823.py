import sys 

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

       
print(maxThree([-3,1,2,-2,5,6])    