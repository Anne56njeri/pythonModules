array = [13,7,6,12]


for index,number in enumerate(array):
    next_greater = -1
    print ('orgindex',index)
    for j in range(+1,len(array)):
       print(number,'===>',next_greater if number < array[j] else number ,'===>', array[j])
      
       
        
