# sort the array
import math 

def pallindum(nums):
     
    large = max(nums)
    big = []
    
    for n in nums:
        if large == n:
            big.append(n)
            
            nums.remove(n)

    firstMax =  large *len(big) 
    

    
    
   
    print(nums)


pallindum([3,1,4,4])    
