array = [13,7,6,12]


for index,number in enumerate(array):
    next_greater = -1
    for j in range(index+1,len(array)):
        next_greater = array[j] if number < array[j]:
        break
    print(number,'===>',next_greater if number > array[j] else  next_greater)
       
      
       
        
