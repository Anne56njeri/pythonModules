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
                   currDiff =  abs(arr[i]-arr[i-1])
                   print('here1')
                   print(arr[i],'-',arr[i-1],'==',currDiff)
               if i < len(arr) -1:

                   currDiff =abs(arr[i] - arr[i+1])
                   print('here2')
                   print(arr[i],'-',arr[i-1],'==',currDiff)
               newDiff = 0 
               if i > 0:
                   newDiff = abs(arr[i]-1 - arr[i-1]) 
                   print('here3')
                   print(arr[i]-1,'-',arr[i-1],'==',newDiff)
               if i < len(arr)-1:
                   newDiff  = abs(arr[i]-1-arr[i+1]) 
                   print('here4')
                   print(arr[i]-1,'-',arr[i+1],'==',newDiff)
               red =  currDiff - newDiff  
               if red > maxred:
                   highest = i 
                   maxred = red 
            if highest == -1:
                return 0 
            else:
                arr[highest] = arr[highest] -1 
                sand -=1 
        diff = 0 
        for i in range(len(arr)-1):
            diff +=abs(arr[i] - arr[i+1])
        return diff                       



                # we get the difference    
                

          



print(food([5, 3, 1, 2, 1]))   


