
# abc-defg-hijklmn
# nml-kjih-gfedcba


def majority (nums):
     length = len(nums)/2
     numbers ={}
     new =[]
     
     for n in nums:
         if n in numbers:
            
             numbers[n]+=1
         else:
              numbers[n]= 1
              new.append(n) 
     
     print(numbers)         
     for n in new:
          print("count",numbers[n])
          print("number",n)
          if numbers[n] > length:
              print(n)
              return n  
        #   else:
        #       print("no")
        #       return "no majority"     
     

majority([3, 3, 4, 2, 4, 4, 2, 4, 4])  