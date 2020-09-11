import sys 

def maxThree(arr):
    if len(arr) < 3:
        return -1 
    maxProduct = -(sys.maxsize -1)
    p