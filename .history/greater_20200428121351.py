array = [13,7,6,12]


for index,number in enumerate(array):
    next_greater = -1
    print ('orgindex',index)
    for j in range(+1,len(array)):
        if number > array[j]:
            print("number",number)   
            print("arrayj",array[j])
        print('index',j)
       
        
