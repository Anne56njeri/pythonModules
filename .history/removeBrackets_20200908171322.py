def remove(str):
  stackA = []
  stackB = []
  total = 0
  for i in range(0,len(str)//2):
      
      stackA.append(str[i])
  for i in range(len(str)//2,len(str)):
      stackB.append(str[i])
  print('A',stackA)
  print('B',stackB)    
  while stackA !=[] and stackB !=[]:
      if stackA[-1] != stackB[-1]:
          stackA.pop()
          stackB.pop()
  if stackA !=[] and stackB !=[]:
      total = len(stackB) + len(stackA)
  elif stackA !=[] or stackB !=[]:
      total =  len(stackA)
      total = len(stackB)
     
  return total    


         

    


print(remove(")(()"))               