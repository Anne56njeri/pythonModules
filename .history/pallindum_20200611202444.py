# sort the array
import math 

def pallindum(nums):
     
    large = max(nums)
    big = []
    countB = 0
    countS = 0
    
    
    for i in range(len(nums)):
        if large == nums[i]:
            countB +=1
            total = nums[i] * countB 
           
        else:
            countS +=1 
            big.append(nums[i]) 

    total2 = countS *  max(big)   
    banner = total2 + to
    print(total2)  

            

            
   


pallindum([3,1,4,])    
