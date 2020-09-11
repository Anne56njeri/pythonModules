# so a number is a power two if it is 
# continually divisble by two 

def power(nums):
    while(nums>2):
        nums = nums/2
        if nums %2 != 0:
            print("false")
            return False
    return True        


    