# sort the array
import math 

def pallindum(nums):
     
    large = max(nums)
    big = []
    print(large)
    
    for n in nums:
        if large == n:
            big.append(n)
            del n


    firstMax =  large *len(big) 
    

    
    
   
    print(nums)


pallindum([3,1,4,4])    
