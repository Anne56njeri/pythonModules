def food(arr):
    # removes the item at index 0 
   sandwiches = arr.pop(0)

   while sandwiches > 0:
       highest = -1 
       maxred = -1 
       for i in range(len(arr)):
           if arr[i] > 0:
               currDiff = 0 
               if i > 0:
                   currDiff = currDiff + abs(arr[i]-arr[i-1])
               if i    

   print(arr)

food([5, 3, 1, 2, 1])   


