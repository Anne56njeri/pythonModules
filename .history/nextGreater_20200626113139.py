# [4,5,2,25]
def nextGreater(arr):
    for i in range(len(arr)):
        
        for j in range(i+1,len(arr)):
            print('i -------->',arr[i]) 
            print('j--->',arr[j])  
            if arr[i] < arr[j]:
                next = arr[j]

            

nextGreater([4,5,2,25])            