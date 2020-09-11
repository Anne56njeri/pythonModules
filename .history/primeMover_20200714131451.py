import math 

def PrimeMover(num):
  # maybe come up with a list of prime numbers from 0 to num+1 
  # return newArr[num]
  # how do we come up with that list 
  # the len of this array should be num+1 
  newArr = []
  count = 0
  numbers = range(2,10**4)
  for i in numbers:
    if is_prime(i) == True:
      #  print(i)
       count +=1
    # print('count',count)  
    if count == num:
      # print(i)
      return i
      
def is_prime(number):
  if number == 1:
    return False
  elif number == 2 or number == 3 or number == 5 or number == 7:
    return True
  elif number % math.sqrt(number) == 0:
    return False
  elif number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number % 7 == 0:
    return False
  else:
    return True 
PrimeMover    