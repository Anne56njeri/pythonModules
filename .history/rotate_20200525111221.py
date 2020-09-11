
def rotate( nums, k):
   if k >0:
       for i in range(k):
           previous = nums[-1]
           print("previous",previous)
           for n in range(len(nums)):
              nums[n],previous = previous,nums[n]
              print






        



rotate([1,2,3,4,5,6,7],3)            