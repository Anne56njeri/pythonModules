def majority (nums):
     length = len(nums)/2
     numbers ={}
     count = 0
     new =[]
     for n in nums:
         if n in numbers:
             count = count + 1
             numbers[n] +=1
         else:
              new.append(n) 
              count[c] = 1
     print(numbers)

majority([3, 3, 4, 2, 4, 4, 2, 4, 4])  