def remove(str):
  stackA = []
  stackB = []
  for i in range(0,len(str)//2):
      
      stackA.append(str[i])
  for i in range(len(str)//2,len(str)):
      stackB.append(str[i])
  while stackA !=[] and stackB !=[]:
      if stackA[-1] != stackB[-1]:
          stackA.pop()
          stackB.pop()
   if sta          
         

    


print(remove(")(()"))               