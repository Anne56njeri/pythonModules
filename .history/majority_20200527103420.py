def majority (nums):
     length = len(nums)/2
     numbers ={}
     count = 0
     new =[]
     number
     for n in nums:
         if n in numbers:
             count = count + 1
             numbers[n] +=1
         else:
              numbers[n] = 1

              new.append(n) 
     for n in new:
          if numbers[n] > length:
              return  
          else:
              print("no majority")      
     

majority([3, 3, 4, 2, 4, 4, 2, 4, 4])  