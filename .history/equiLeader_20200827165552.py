def equi(A):
    # return the number of equal leaders that both occur in the sequences 
    # first find the equileader 
    # an equileader is an index such that when two sequences are formed 
    # the two sequences have the same  leader 
    # 0,1,2,3,4,5
    store = {}
     = -1
    count = 0
    for i in A:
        if i in store:
            store[i] +=1 
        else:
            store[i] = 1 
         
     
           
        
print(equi([4, 4, 2, 5, 3, 4, 4, 4] ))    