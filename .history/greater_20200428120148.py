array = [13,7,6,12]
for index,number in enumerate(array):
    next_greater = -1
    for secondnum in range(index+1,len(array)):
        if number > array[secondnum]:
            next_greater = -1
            print(number,'==>',next_greater)
        elif number < array[secondnum]:
            next_greater = array[secondnum]
            print(number,'===>',next_greater)
        
