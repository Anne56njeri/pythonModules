# sort the array
import math 

def pallindum(nums):
    nums2 = sorted(nums)
    count  = 0 
    large = max(nums2)
    big = []
    for n in nums:
        if large == n:
            big.append(n)

    
    
   
    print(max(nums2))


pallindum([3,1,4,4])    
