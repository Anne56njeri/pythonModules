array = [13,7,6,12]
for index,number in enumerate(array):
    next_greater = -1
    for secondnum in range(index+1,len(array)):
        if number > array[-3:]:
            print(number)
        
