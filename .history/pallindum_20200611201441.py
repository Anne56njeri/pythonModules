# sort the array
import math 

def pallindum(nums):
     
    large = max(nums)
    big = []
    print(large)
    
    for n in nums:
        if large == n:
            nums.remove(n)
            big.append(n)
            


    firstMax =  large *len(big) 
    

    
    
   
    print(big)


pallindum([3,1,4,4])    
