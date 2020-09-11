array = [13,7,6,12]
for index,number in enumerate(array):
    print('num--',number)
    next_greater = -1
    for secondnum in range(index+1,len(array)):
        if number > array[j]:
            next_greater = -1
            print(number,'==>',next_greater)
        elif number < array[j]:
            next_greater = array[j]
            print(number,'===>',next_greater)
        
