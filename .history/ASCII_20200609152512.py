def ASCIIConversion(s):
  s = s.split()
  num = ""
  for i in s:
    print('i---->',i)
    for j in i:
      print('j---->',j)
      num += str(ord(j))
    num +=" "
  print(num)   
  # code goes here
  return num
ASCIIConversion("dog") 