def missing(arr):
    # goal is to find the smallest int missing that is greater than 0
    # I would a range from 1 to max value in the arr 
    # o(n)
    # the number can't be a negative 
    if len(arr) == 0:
        return 0 
    else:
        newArr = range(0)    