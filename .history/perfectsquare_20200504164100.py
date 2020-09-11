import math 

def perfect(sq):
   root= int(math.sqrt(sq))
   root1 = math.pow(root,2)
   print(sq*0.5,'0.5')
   print(root,'root')
   
   if root1 == sq:
       print(sq,'is a perfect square')
       print (root1,'square')
       next = math.pow(root + 1,2)
       print (next,'next')
   else:
       
       print(root1)
       print('Its not a perfect square')    

perfect(144)   