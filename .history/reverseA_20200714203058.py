'''
Given array A consisting of N integers, return the reversed array
'''
def array(arr):
    i = 0
    j = len(arr)-1
    while i < len(arr)-1 and j > 0:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i +=1
        j -=1
        print(arr)    



array([1, 2, 3, 4, 5, 6])    
