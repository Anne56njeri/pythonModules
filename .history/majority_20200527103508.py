def majority (nums):
     length = len(nums)/2
     numbers ={}
     count = 0
     new =[]
     
     for n in nums:
         if n in numbers:
            
             numbers[n] +=1
         else:
              numbers[n] = 1

              new.append(n) 
     for n in new:
          if numbers[n] > length:
              print(n)
              return n  
          else:
              print()
              return "no majority"     
     

majority([3, 3, 4, 2, 4, 4, 2, 4, 4])  