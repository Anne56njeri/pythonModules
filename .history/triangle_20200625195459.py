# this function is meant to print a triangle 

def triangle():
    # outer loop is for the rows --> 4 
    for i in range(0,4):
        # inner loop is for colums --> 4
        print('i-->',i)
       for j in range(0,i+1):
           print('j-->')
           print('*')
           

triangle()            
    