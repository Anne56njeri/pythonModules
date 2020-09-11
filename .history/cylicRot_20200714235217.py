# given an array rotate it k times to the right 
def rotate(arr,k):
    # first I'd rotate the array once 
    # so how do we rotate the array 
    # we move the last element to the firs place and
    # the rest follow suit 
    # [1,2,3,4]
    # [4,1,2,3]
    # [4,2,3,1]
    # [4,1,3,2]
    # [4,1,2,3]
    # [4,1,2,3]
    # all we are doing is swapping the elements
    count = 0
    while count <= k:
        for i in range(len(arr)):
            k = len(arr) - 1
            print('k',k,'i',i)
            arr[i],arr[k] = arr[k],arr[i]
        count +=1
    print(arr)    
rotate(3, 8, 9, 7, 6], 3)    
