def NonrepeatingCharacter(str):
  char_order = []
  #  this is a set can't contain duplicate elements ...
  counts = {} 
  
  # loop through the str 

# oop through this 
  for c in str:
    #   if c is in  counts increment the counter 
    if c in counts:
      counts[c] += 1
    else:
      counts[c] = 1   
      char_order.append(c)
  for c in char_order:
    if counts[c] == 1:
      return c
    
NonrepeatingCharacter("banana")  