def search(list,n):
    # lower bound
    l = 0 
    # upper bound
    u = len(list)-1 
    
    while l <=  u:
        # find the mid value
        mid = (l+u) // 2 # double slash will give you int value 
        if list[mid] == n :
            print(mid)
            return True
        else:
            # compare the if its greater than the mid value
            if n > list[mid] :
                l = mid 
            else:
                u = mid 
                

search([4,7,8,12,45,99],8)


