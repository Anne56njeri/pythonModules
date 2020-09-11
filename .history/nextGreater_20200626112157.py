# [4,5,2,25]
def nextGreater(arr):
    for i in range(len(arr)):
        print('i------>',i)

        for j in range(i+1,len(arr)):
            if(arr[i] > arr[j]):
                print(arr[i],'--->'arr[j])
                

            

nextGreater([4,5,2,25])            