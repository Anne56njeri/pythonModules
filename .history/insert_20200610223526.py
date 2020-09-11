# nums is a list 
# find where n is to be inserted 
# soo,you loop through the array 
# the array is sorted 
# to know the position you should check whethere n is greater than nums[i]
# continue the loop as you check 

def Insert(nums,n):
    i = 0
    while i < len(nums):
        if n != nums[i]:
            if n > nums[i]:
                i +=1
                print("i--->",i)
            elif n > num[len(nums)-1]:
                print("i---")
                return i+1  
            else:
                print("i--->",i)
                print("i",i+1)
                return i


               
        else:
            print(i)
            return i        



      
Insert([1,3,4,6],7)               
   


