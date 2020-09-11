def ASCIIConversion(s):
#   s = s.split()
  num = ""
  for i in s:
    print('i---->',i)
    num += str(ord(i))

    num +=" "
  print(num)   
  # code goes here
  return num
ASCIIConversion("dog") 