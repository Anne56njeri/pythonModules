# sort the array
import math 

def pallindum(nums):
     
    large = max(nums)
    big = []
    print(large)
    
    i = 0 
    while i < len(nums):
        if large == nums[i]:
            big.append(nums[i])
            nums.remove(nums[i])
            i+=1

    for i in range(len(nums)):
        
            
            


    firstMax =  large *len(big) 
    

    
    
   
    print(big)


pallindum([3,1,4,4])    
