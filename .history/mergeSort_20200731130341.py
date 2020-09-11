# MERGE SORT 
# --> Recursive 
# ---> divide and conquer 
# ---> If the problem is too big , break it down 
# --> if its a single element its a small problem 
# ---> recursive algorithm 
# Takes two a params (low,high)
# if low < high
'''
    if (l< high)
    mid = l+h // 2
    left hand side(perform sort recursively)
    and same for right 
    mergeSort(l,mid)
    mergeSort(mid+1,h)
    perform merge
'''

def merge(arr):
