def search(list,n):
    # lower bound
    l = 0 

    # upper bound
    # last index
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
                print("new lower bound",list[])
                l = mid+1
            else:
                u = mid-1
    return False            

print(search([4,7,8,12,45,99],10))


