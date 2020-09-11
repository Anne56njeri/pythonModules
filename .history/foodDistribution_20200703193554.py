def food(arr):
   # removes the item at index 0 
   sandwiches = arr.pop(0)
   # this loop runs only when sandwiches are greater than 0,otherwise we exit the while loop  
   while sandwiches > 0:
       highest = -1 
       maxred = -1
       # looping throught the hunger levels
       for i in range(len(arr)):
           # checking if elements in the array are greater than 0  
           if arr[i] > 0:
               currDiff = 0
               # if index we are at ain't 0 
               if i > 0:
                   # we get the difference between  adjacent pairs 
                   currDiff = currDiff + abs(arr[i]-arr[i-1])
                   print(arr[i],'-',arr[i-1])
               if i < len(arr) -1:
                   newDiff = abs(arr[i]-1 - arr[i+1]) 
                # we get the difference    
                red = currDiff - newDiff 

          



print(food([5, 3, 1, 2, 1]))   


