def plusOne(nums):
    end = len(nums) -1
    nums[end] = nums[end] +1 
    hmm = [int(i) for i in str(nums[end])]
    print(hmm)
    # print(nums)



plusOne([9])    