import sys 

def maxThree(arr):
    if len(arr) < 3:
        return -1 
    maxProduct = -(sys.maxsize -1)
    print(maxProduct) 
maxThree([-3,1,2,-2,5,6])    