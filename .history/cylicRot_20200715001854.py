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
    count = 0
    while count <=  K:
       
        newArr.append(A[-1])
        newArr.extend(A[:-1])
        count +=1 

        
        print(newArr)
    # while count <= K:
        

           
        


      
rotate([3, 8, 9, 7, 6], 3)    
