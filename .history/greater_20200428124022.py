array = [13,7,6,12]


for index,number in enumerate(array):
    next_greater = -1
    for j in range(+1,len(array)):
       if number < array[j]:
           next_greater = array[j]
       print(number,'===>',next_greater if number > array[j] else next_greater)
       break
      
       
        
