# sort the array
import math 

def pallindum(nums):
    nums2 = sorted(nums)
    
    large = max(nums2)
    big = []
    

    for n in nums:
        if large == n:
            del n
            big.append(n)

    firstMax =  large *len(big) 
    secondMax =  

    
    
   
    print(firstMax)


pallindum([3,1,4,4])    
