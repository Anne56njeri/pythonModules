def ASCIIConversion(s):
  s = s.split()
  num = ""
  for i in s:
      print(''i)
    for j in i:
      num += str(ord(j))
    num +=" "
  print(num)   
  # code goes here
  return num
ASCIIConversion("dog") 