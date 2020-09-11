def food(arr):
    # removes the item at index 0 
   sandwiches = arr.pop(0)

   while sandwiches > 0:
       highest = -1 
       maxred = -1 
    #    we loop through the array as long as sandwiches is  > 0
       for i in range(len(arr)):
           if arr[i] > 0:
               currDiff = 0 
               if i > 0:
                   currDiff = currDiff + abs(arr[i]-arr[i-1])
                   print(currDiff,'=',arr[i],'-')
               if i < len(arr)-1:
                   currDiff = currDiff + abs(arr[i] - arr[i+1])
               newDiff = 0 
               if i > 0:
                   newDiff += abs(arr[i]-1 - arr[i-1])
               if i < len(arr)-1:
                   newDiff = abs(arr[i]-1 - arr[i+1])  
               red =   currDiff - newDiff
               if red > maxred :
                   highest = i 
                   maxred = red 

       if highest == -1:
            return 0 
       else:
           arr[highest] = arr[highest] - 1
           sandwiches -=1 

   diff = 0 
   for i in range(len(arr) -1):
       diff +=abs(arr[i] - arr[i+1])
   return diff           



print(food([5, 3, 1, 2, 1]))   


