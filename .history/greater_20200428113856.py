    
for index,number in enumerate(array):
    next_greater = -1
    for j in range(index+1, len(array)):
        # starting from the next index, check whether 
        # there is a number greater than the current
        if number < array[j]:
            next_greater = array[j]
            break     
    print (number ," ====> ", next_greater)