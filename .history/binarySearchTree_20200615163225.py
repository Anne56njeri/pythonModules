def search(list,n):
    l = 0 
    u = len(list)-1 

    while l <=  u:
        mid = (l+u) // 2 # double slash will give you int value 
        if list[mid] == n :
            print
            return True
        else:
            if n > list[mid] :
                l = mid 
            else:
                u = mid 




