def majority (nums):
     length = len(nums)/2
     numbers ={}
     count = 0
     new =[]
     for n in range(len(nums)):
         if n in numbers:
             count = count + 1
              
          else:
              new.append(n)   

     print(length)

majority([3, 3, 4, 2, 4, 4, 2, 4, 4])  