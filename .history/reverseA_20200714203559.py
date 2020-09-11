'''
Given array A consisting of N integers, return the reversed array
'''
def array(arr):
    i = 0
    j = len(arr)-1
    while i <= len(arr) // 2 and j > 0:
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i +=1
        j -=1
        print(arr) 
# iterate over the firs  half of the array and exchange the elements with the second part of the array 
 
def reverse(arr):
    n = len(arr)
    for i in range(n //2):
        # moves from the end of the array 
        k = n - i -1
        # print(i)
        print(k)





reverse([1, 2, 3, 4, 5, 6,7])    
