import statistics.median

def MovingMedian(arr):

 answer = []
 window = arr[0]

 for i in range(1,len(arr)):
     print('i',i)
     if i <= window:
        # like getting a sub string 
         val = median(sorted(arr[1:i+1]))
         
     else:
         val = median(sorted(arr[i-window+1:i+1]))
         print(val)

print(MovingMedian([3,1,3,5,10,6,4,3,1])) 