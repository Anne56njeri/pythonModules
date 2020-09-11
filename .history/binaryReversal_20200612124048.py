def BinaryReversal(s):
  n = bin(int(s))
  n=n[2:]
  if len(n)%8 == 0:
    N = len(n)//8
  else:
    N = len(n)//8+1
  k=str()
  for i in range(len(n)):
    k+=n[-i-1]
  while len(k)<N*8:
    k+="0"
  
  # code goes here
  return int(k,2) 
BinaryReversal("")
