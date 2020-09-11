# [4,5,2,25]
def nextGreater(arr):
    for i in range(len(arr)):
        print('i---->',arr[i])

        for j in range(i,len(arr)):
            print('j--->',arr[j])

nextGreater([4,5,2,25])            