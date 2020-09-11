# given an array rotate it k times to the right 
def rotate(A,K):
    # first I'd rotate the array once 
    # so how do we rotate the array 
    # we move the last element to the firs place and
    # the rest follow suit 
    # moving elements to the right in an array 
    # [3,8,9,7,6]
    # 3 ---> 0 now 3 ---> 1
    # 8 ---> 1 now 8 ---> 2
    #  A[0] = A[len(A)-1]

    # [6 ,3,8,9,7]
    # what do you notice that   A[i] = A[i+1]
    # [lst[-1]] + lst[:-1]   
   if len(A) == 0:
       return []
   elif len(A) == 1:
        return A
  elif K <= 0:
        return A
  else:    
      count = 0
      while count <  K:
          newArr=[]
          newArr.append(A[-1])
          newArr.extend(A[:-1])
          A = newArr
          count +=1 
        
    return newArr
    
        

           
        


      
print(rotate([1,2,3], 0))   
