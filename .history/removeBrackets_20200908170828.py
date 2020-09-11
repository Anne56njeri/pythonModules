def remove(str):
  stackA = []
  stackB = []
  for i in range(0,len(str)//2):
      
      stackA.append(str[i])
  for i in range(len(str)//2,len(str)):
      stackB.append(str[i])
  print(stackA)
  print(stackB)    
         

    


print(remove(")(()"))               