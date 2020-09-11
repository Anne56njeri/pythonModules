# [4,5,2,25]
def nextGreater(arr):
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print('i---->',arr[i])
            print('j--->',arr[j])