
def rotate( nums, k):
   
    if k >= 0:
        # get the last elements
        first_nums = nums[:-k]
        last_nums = nums[-k:]
       
    print(last_nums + first_nums)




        



rotate([1,2,3,4,5,6,7],3)            