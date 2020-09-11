def BinaryReversal(s):
  n = bin(int(s))
  print(n[2:])
  n=n[2:]

  if len(n)%8 == 0:
    N = len(n)//8
    print('N',N)
  else:

    N = len(n)//8+1
    print('N',N)

  k=str()
  
  print('n at this point',n)

  for i in range(len(n)):
    k+=n[-i-1]
  print('k',k)

  while len(k)<N*8:
    k+="0"
    print("k in while",k))
  print(int(k,2))
  # code goes here
  return int(k,2) 

BinaryReversal("4567")
