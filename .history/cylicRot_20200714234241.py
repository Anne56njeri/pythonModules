# given an array rotate it k times to the right 
def rotate(arr,k):
    # first I'd rotate the array once 
    # so how do we rotate the array 
    # we move the last element to the firs place and
    # the rest follow suit 
    # [1,2,3,4]
    # [4,1,2,3]
    newArr = []
    for i in range(len(arr)):
        k = len(arr) - 1
        arr[i] = arr[k]
        
rotate([1,2,3,4],4)    
