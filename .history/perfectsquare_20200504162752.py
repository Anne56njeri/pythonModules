import math 

def perfect(sq):
   root= math.sqrt(sq)
   root1 = math.pow(root,2)
   
   if root1 == sq:
       print(sq,'is a perfect square')
       next = math.pow(root + 1,2)
       print (next,'next')
   else:
       
       print(root1)
       print('Its not a perfect square')    
   print(root)

perfect(155)   