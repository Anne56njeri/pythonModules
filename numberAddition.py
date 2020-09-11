def NumberAddition(str):
  number = ""
  i = 0 
  total = 0
  # base cases
  
  str = str + "k"

  while i < len(str):
    if str[i].isdigit():
      number +=str[i]
    else:
      if number != '':
        total +=int(number)
      number =""   
    i+=1
  return total
