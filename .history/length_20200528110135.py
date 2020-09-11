 def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])