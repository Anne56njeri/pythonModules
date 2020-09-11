def remove(str):
  opening = 0 
  complete = 0 
  total = len(str)
  for i in str:
      if i == "(":
          opening +=1 
      elif i == ")" and opening > 0:
          opening -=1 
          complete +=2 
  return total - com           


         

    


print(remove(")(()"))               