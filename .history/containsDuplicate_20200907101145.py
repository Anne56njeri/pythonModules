def duplicate(nums,k,t):
#    complexity is o()

    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if abs(nums[i] - nums[j]) <= t and j - i <= k:
               return True 
    return False           
          
print(duplicate([1,5,9,1,5,9],2,3))               
                


