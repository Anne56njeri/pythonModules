# [4,5,2,25]
def nextGreater(arr):
    # next = 0 

    for i in range(len(arr)):
        next = -1

        for j in range(i+1,len(arr)):
            # print('i -------->',arr[i]) 
            # print('j--->',arr[j])  
            if arr[i] < arr[j]:
                next = arr[j]
                # break
        print(arr[i],'---->',next)    

            

nextGreater([4,5,2,25])            