# sort the array
import math 

def pallindum(nums):
    nums2 = sorted(nums)
    
    large = max(nums)
    big = []
    

    for n in nums:
        if large == n:
            
            big.append(n)
            del n

    firstMax =  large *len(big) 
    

    
    
   
    print(nums)


pallindum([3,1,4,4])    
