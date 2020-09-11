def MovingMedian(arr):

 answer = []
 window = arr[0]

 for i in range(1,len(arr)):
     print('i',i)
     if i <= window:
        # like getting a sub string 
         val = arr[1:i+1]
         print(val)
     else:
         val = arr

print(MovingMedian([3,1,3,5,10,6,4,3,1])) 