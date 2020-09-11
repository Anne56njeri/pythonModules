array = [13,7,6,12]
for index,number in enumerate(array):
    next_greater = -1
    print ('orgindex',index)
    for j in range(index+1,len(array)):
        if number > array[j]:
            print("yes")
        print('index',j)
       
        
