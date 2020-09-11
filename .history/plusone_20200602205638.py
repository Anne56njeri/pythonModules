def plusOne(nums):
    number = ""
    for i in nums:
        number += str(i)
    newNumber = int(number) +1   
    newArr =  [int(i) for i in str(newNumber)]

    print(newArr)

     
    
    #    newArr = [int(i) for i in str(nums[end])]

        


    
    



plusOne([1,2,3])    