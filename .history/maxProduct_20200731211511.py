import sys 

def maxThree(arr):
    if len(arr) < 3:
        return -1 
    maxProduct = -(sys.maxsize -1)
    print(maxProduct) 
    n = len(arr)
    for i in range(0,n-2):
        
        for j in range(i+1,n-1):
            print('j--->',j)
            for k in range(j+1,n):
                print('k--->',k)

       
maxThree([-3,1,2,-2,5,6])    