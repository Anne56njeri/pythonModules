# [4,5,2,25]
def nextGreater(arr):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if(arr[i] < arr[j]):
                print(arr[i],'--->',arr[j])
                break
            else:
                print(arr[i],'--->',-1)    

            

nextGreater([4,5,2,25])            