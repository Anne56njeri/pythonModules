# nums is a list 
# find where n is to be inserted 
# soo,you loop through the array 
# the array is sorted 
# to know the position you should check whethere n is greater than nums[i]
# continue the loop as you check 

def Insert(nums,n):
    for i in range(len(nums)):
        if n != nums[i]:
            if n > nums[i]-1:
                print(i+1)
            else:
                


           
        else:
             print(i)


      
Insert([1,3,4,6],5)               
   


