def duplicate(nums,k,t):
#    complexity is o(n)2


    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if abs(nums[i] - nums[j]) <= t and j - i <= k:
               return True 
    return False           
def duplicate1(nums,k,t):
    for i in range(len(nums)):
        for j in range()



print(duplicate1([1,5,9,1,5,9],2,3))               
                


