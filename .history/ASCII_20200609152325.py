def ASCIIConversion(s):
  s = s.split()
  num = ""
  for i in s:
    for j in i:
      num += str(ord(j))
    num +=" "
  print(num)   
  # code goes here
  return num
  