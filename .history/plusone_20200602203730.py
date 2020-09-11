def plusOne(nums):
    end = len(nums) -1
    nums[end] = nums[end] +1 
    if nums[end] >= 10:
        
        for i in str(nums[end]):
            print(i)
            nums[end] = int(i)


    
    print(nums)



plusOne([1,9])    