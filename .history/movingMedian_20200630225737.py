def MovingMedian(arr):

 answer = []
 window = arr[0]
 for i in range(1,len(arr)):
     print('',i)
     if i <= window:
         val = arr[1:i+1]
print(MovingMedian([3,1,3,5,10,6,4,3,1])) 